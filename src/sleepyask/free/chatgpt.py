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

def ask_questions(configs, questions : list, output_file_path: str, verbose: bool) -> None:
    question_queue = queue.Queue()

    def loader_worker():
        if verbose: print(f"[sleepyask] Loading questions into queue")
        # Check for failed questions
        check_set = set()
        if Path(output_file_path).is_file():
            with open(output_file_path) as f:
                asked_questions = []
                for line in f:
                    asked_questions.append(json.loads(line))
                max_index = 0

                for question in asked_questions:
                    check_set.add(question["question_number"])
                    max_index = max(max_index, question["question_number"])

        for index in range(0, len(questions)):
            if not index in check_set:
                question_queue.put({"question": questions[index], "question_number": index})

        if question_queue.empty(): 
            print("[sleepyask] All questions exhausted")
            print("""
***     DONE ASKING ALL QUESTIONS       ***""")
                    

    def asker_worker(index, config):
        if verbose: print(f"[sleepyask {index}] Logging into ChatGPT with user credentials")
        chatbot = Chatbot(config=config)
        if verbose: print(f"[sleepyask {index}] Successfully logged in")

        while True:
            question = question_queue.get()
            logging.disable(logging.ERROR)
            
            if verbose: print(f"[sleepyask {index}] Asking:", question["question"])
            try:
                message = ""
                for data in chatbot.ask(question["question"]):
                    message = data["message"]
                logging.disable(logging.NOTSET)
            except:
                if verbose: print(f"[sleepyask {index}] Failed to ask questions. Will try again in 15 minutes")
                question_queue.put(question)
                return

            if verbose: print(f"[sleepyask {index}] Received:", message)

            dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            row_to_append = {"date_time": dt_string, "question_number": question["question_number"], "question": question["question"],"response": __clean_str_for_json(message)}
            __append_to_file(output_file_path, row_to_append)
            question_queue.task_done()

    for index, config in enumerate(configs):
        threading.Thread(target = asker_worker, daemon=True, kwargs={'index': index, 'config': config}).start()
    threading.Thread(target = loader_worker, daemon=True).start()

    question_queue.join()