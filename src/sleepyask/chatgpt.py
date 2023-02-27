from revChatGPT.V1 import Chatbot
import json
from pathlib import Path
import logging
from datetime import datetime

def __append_to_file(output_file_path: str, data):
    with open(output_file_path, 'a') as outfile:
        outfile.write(json.dumps(data))
        outfile.write("\n")
        outfile.close()


def __clean_str_for_json(text: str):
    return text.replace("\"", "\'")


def ask_all_questions(config, questions : list, output_file_path : str, verbose:bool) -> None:
    if verbose: print("[sleepyask] Logging into ChatGPT with user credentials")
    chatbot = Chatbot(config=config)
    if verbose: print("[sleepyask] Successfully logged in")

    def ask_chat_gpt(question: str) -> str:
        question = str(question)
        
        if verbose: print("[sleepyask] Asking:", question)

        logging.disable(logging.ERROR)
        try:
            message = ""
            # prev_text = ""
            for data in chatbot.ask(question):
                message = data["message"]
        except json.decoder.JSONDecodeError: pass
        logging.disable(logging.NOTSET)
        
        if verbose: print("[sleepyask] Received:", message)
        return message
    
    last_index = -1
    if Path(output_file_path).is_file():
        with open(output_file_path) as f:
            last_index = eval(f.readlines()[-1])["question_number"]

    for index, question in enumerate(questions):
        if index <= last_index: continue

        chatgpt_response = ask_chat_gpt(question)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        row_to_append = {"date_time": dt_string, "question_number": index, "question": question,"response": __clean_str_for_json(chatgpt_response)}
        __append_to_file(output_file_path, row_to_append)
