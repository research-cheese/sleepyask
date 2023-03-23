from sleepyask.openai.chatgpt import ask_questions
import traceback
import logging

def ask(configs : list, questions : list, output_file_path : str, verbose: bool = False, model : str = "gpt-3.5-turbo", system_text : str | None = None, temperature : float | None = 1, max_tokens : int | None = 2048):
    '''
    `config` should be a list containing your ChatGPT access tokens / email and password\n
    `questions` should contain a list of questions you would like ChatGPT to answer.\n
    `output_file_path` should be the file path where you would like your responses to be saved.\n
    '''
    redo = True
    while redo:
        if not isinstance(questions, list): raise ValueError("[questions] should be a list")

        try: ask_questions(configs=configs, questions=questions, output_file_path=output_file_path, verbose=verbose, model=model, system_text=system_text, temperature=temperature, max_tokens=max_tokens)
        except Exception as e: 
            logging.error(traceback.format_exc())