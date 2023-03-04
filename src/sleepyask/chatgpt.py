from revChatGPT.V1 import Chatbot
import json
from pathlib import Path
import logging
from datetime import datetime
import threading
import queue

def __append_to_file(output_file_path: str, data):
    with open(output_file_path, 'a') as outfile:
        outfile.write(json.dumps(data))
        outfile.write("\n")
        outfile.close()


def __clean_str_for_json(text: str):
    return text.replace("\"", "\'")


def ask_all_questions(config, questions : list, output_file_path : str, verbose:bool) -> None:
    ask_questions_multi(configs=[config], questions=questions, output_file_path=output_file_path, verbose=verbose)

def ask_questions_multi(configs, questions : list, output_file_path: str, verbose: bool) -> None:
    question_queue = queue.Queue()

    def loader_worker():
        print(f"[sleepyask] Loading questions into queue")
        # Check for failed questions
        if Path(output_file_path).is_file():
            with open(output_file_path) as f:
                asked_questions = []
                for line in f:
                    asked_questions.append(json.loads(line))
                max_index = 0

                check_set = set()
                for question in asked_questions:
                    check_set.add(question["question_number"])
                    max_index = max(max_index, question["question_number"])

                whole = set(range(0, len(questions)))
                question_list = whole - check_set

                if len(question_list) == 0: quit()
                
                for index in question_list:
                    question_queue.put({"question": questions[index], "question_number": index})
                    

    def asker_worker(index, config):
        if verbose: print(f"[sleepyask {index}] Logging into ChatGPT with user credentials")
        chatbot = Chatbot(config=config)
        if verbose: print(f"[sleepyask {index}] Successfully logged in")

        while True:
            question = question_queue.get()
            logging.disable(logging.ERROR)
            
            print(f"[sleepyask {index}] Asking:", question)

            message = ""
            for data in chatbot.ask(question["question"]):
                message = data["message"]
            logging.disable(logging.NOTSET)

            if verbose: print(f"[sleepyask {index}] Received:", message)

            dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            row_to_append = {"date_time": dt_string, "question_number": question["question_number"], "question": question["question"],"response": __clean_str_for_json(message)}
            __append_to_file(output_file_path, row_to_append)
            question_queue.task_done()

    for index, config in enumerate(configs):
        threading.Thread(target = asker_worker, daemon=True, kwargs={'index': index, 'config': config}).start()
    threading.Thread(target = loader_worker, daemon=True).start()

    question_queue.join()