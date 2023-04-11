import json
from pathlib import Path
from datetime import datetime
import threading
import queue
import logging
import traceback
import time

def __append_to_file(output_file_path: str, data):
    with open(output_file_path, 'a') as outfile:
        outfile.write(json.dumps(data))
        outfile.write("\n")
        outfile.close()


def __clean_str_for_json(text: str):
    return text
    return text.replace("\"", "\'")


def ask_questions(configs : list, questions : list, output_file_path : str, verbose: bool = False, model : str = "gpt-3.5-turbo", system_text : str | None = None, temperature : float | None = 1, max_tokens : int | None = 2048) -> None:
    question_queue = queue.Queue()
    save_queue = queue.Queue()

    def loader_worker():
        if verbose:
            print(f"[sleepyask] Loading questions into queue")
        # Check for failed questions
        check_set = set()
        if Path(output_file_path).is_file():
            with open(output_file_path) as f:
                asked_questions = []
                index = 0
                for line in f:
                    try:
                        asked_questions.append(json.loads(line))
                    except:
                        print(f"Output file is incorrectly formatted {index}")
                    index = index + 1
                max_index = 0

                for question in asked_questions:
                    check_set.add(question["question_number"])
                    max_index = max(max_index, question["question_number"])

        for index in range(0, len(questions)):
            if not index in check_set:
                question_queue.put(
                    {"question": questions[index], "question_number": index})

        if question_queue.empty():
            print("[sleepyask] All questions exhausted")
            print("\n***     DONE ASKING ALL QUESTIONS       ***")

    def saver_worker():
        while True:
            if save_queue.empty(): continue
            to_add = save_queue.get()
            __append_to_file(output_file_path, to_add)
            save_queue.task_done()

    def asker_worker(index, config):
        import openai
        openai.organization = config["organization"]
        openai.api_key = config["api_key"]

        succeed = True
        while succeed:
            if question_queue.empty(): succeed = False
            question = question_queue.get()
            message = ''
            if verbose:
                print(f"[sleepyask {index}] Asking:", question["question"])
            try:
                messages = [
                    {"role": "user", "content": question["question"]},
                ]

                if (system_text != None):
                    messages.insert(
                        0, {"role": "system", "content": system_text})

                message = openai.ChatCompletion.create(
                    temperature=temperature,
                    max_tokens=max_tokens,
                    model=model,
                    messages=messages
                )

                actual_model = message["model"]
                usage = message["usage"]
                message = message["choices"][0]["message"]["content"]

                if verbose:
                    print(f"[sleepyask {index}] Received:", message)

                dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                row_to_append = {"model": actual_model, "temperature": temperature, "max_tokens": max_tokens, "date_time": dt_string, "question_number":
                                 question["question_number"], "question": question["question"], "system_text": str(system_text), "response": __clean_str_for_json(message), **usage}
                save_queue.put(row_to_append)

            except KeyboardInterrupt:
                succeed = False
                break
            except openai.error.AuthenticationError:
                logging.error(traceback.format_exc())
                question_queue.put(question)
                time.sleep(120)

            question_queue.task_done()

    thread_refs = []
    for index, config in enumerate(configs):
        for num in range(config["count"]):
            t = threading.Thread(target=asker_worker, daemon=True, kwargs={
                'index': index * config["count"] + num, 'config': config})
            thread_refs.append(t)
            t.start()

    loader = threading.Thread(target=loader_worker, daemon=True)
    saver = threading.Thread(target=saver_worker, daemon=True)
    thread_refs.append(loader)
    thread_refs.append(saver)
    
    loader.start()
    saver.start()

    question_queue.join()
    save_queue.join()

    for t in thread_refs:
        t.join()
