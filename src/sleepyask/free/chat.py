import schedule
import sleepyask.free.chatgpt
import traceback
import logging

def ask(configs : list, questions : list, output_file_path : str, verbose: bool = False):
    '''
    `config` should be a list containing your ChatGPT access tokens / email and password\n
    `questions` should contain a list of questions you would like ChatGPT to answer.\n
    `output_file_path` should be the file path where you would like your responses to be saved.\n
    '''
    if not isinstance(questions, list): raise ValueError("[questions] should be a list")
    def func() -> None:
        try: sleepyask.free.chatgpt.ask_questions(configs=configs, questions=questions, output_file_path=output_file_path, verbose=verbose)
        except Exception as e: logging.error(traceback.format_exc())
    
    schedule.every(15).minutes.do(func)
    schedule.every(15).minutes.do(func)

    func()
    while True: schedule.run_pending()