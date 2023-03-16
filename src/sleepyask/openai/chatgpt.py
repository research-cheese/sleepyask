import json
from pathlib import Path
from datetime import datetime
import threading
import queue
import logging 
import traceback


def __append_to_file(output_file_path: str, data):
    with open(output_file_path, 'a') as outfile:
        outfile.write(json.dumps(data))
        outfile.write("\n")
        outfile.close()


def __clean_str_for_json(text: str):
    return text.replace("\"", "\'")


def ask_questions(configs, questions: list, output_file_path: str, verbose: bool, model) -> None:
    question_queue = queue.Queue()

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
            print("""
***     DONE ASKING ALL QUESTIONS       ***""")

    def asker_worker(index, config):
        import openai
        openai.organization = config["organization"]
        openai.api_key = config["api_key"]

        succeed = True
        while succeed:
            question = question_queue.get()
            message = ''
            if verbose:
                print(f"[sleepyask {index}] Asking:", question["question"])
            # logging.disable(logging.ERROR)
            try:
                message = openai.ChatCompletion.create(
                    model=model,
                    messages=[
                        {"role": "user", "content": question["question"]},
                    ]
                )
                actual_model = message["model"]
                usage = message["usage"]
                message = message["choices"][0]["message"]["content"]

                if verbose:
                    print(f"[sleepyask {index}] Received:", message)

                dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                row_to_append = {"model": actual_model, "date_time": dt_string, "question_number":
                                 question["question_number"], "question": question["question"], "response": __clean_str_for_json(message), **usage}
                __append_to_file(output_file_path, row_to_append)

            except openai.error.AuthenticationError:
                logging.error(traceback.format_exc())
                question_queue.put(question)
                succeed = False

            question_queue.task_done()

    thread_refs = []
    for index, config in enumerate(configs):
        for num in range(config["count"]):
            t = threading.Thread(target=asker_worker, daemon=True, kwargs={
                'index': index * config["count"] + num, 'config': config})
            thread_refs.append(t)
            t.start()

    t = threading.Thread(target=loader_worker, daemon=True)
    thread_refs.append(t)
    t.start()

    question_queue.join()

    for t in thread_refs:
        t.join()
