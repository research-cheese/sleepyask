import schedule
import sleepyask.chatgpt
import traceback
import logging

def sleepy_ask(config, questions : list, output_file_path : str, verbose : bool=False):
    '''
    `config` should contain your ChatGPT email and password.\n
    `questions` should contain a list of questions you would like ChatGPT to answer.\n
    `output_file_path` should be the file path where you would like your responses to be saved.\n
    '''
    if not isinstance(questions, list): raise ValueError("[questions] should be a list")
    def func() -> None:
        try: sleepyask.chatgpt.ask_all_questions(config=config, questions=questions, output_file_path=output_file_path, verbose=verbose)
        except Exception as e: logging.error(traceback.format_exc())
    
    schedule.every(1).hours.do(func)
    schedule.every(1).hours.do(func)

    func()
    while True: schedule.run_pending()