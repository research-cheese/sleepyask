import time
import queue
import json
import asyncio

from openai_async import openai_async

# TODO: Shouldn't be that hard to extend to other OpenAI functions but chat is the only one I'm familiar with atm
class Sleepyask:
    """
    This class provides functions which use ayncio to ask multiple questions to ChatGPT simultaneously.
    This allows users to aggregate a large number of responses from ChatGPT.
    """

    def __init__(self, configs : dict ={}, rate_limit: int = 5, api_key: str = "", timeout: int = 100, out_path : str = "", verbose: bool = False):
        """
        `configs` a dict containing parameters which will be part of the payload such as model, temperature, etc
        `rate_limit` the maximum number of questions you would like to ask a minute.
        `api_key` OpenAI API key
        `timeout` the amount of time to wait before timing out
        `out_path` the path in which the responses will be outputted
        """
        self.configs = configs
        self.rate_limit = rate_limit
        self.api_key = api_key
        self.timeout = timeout
        self.out_path = out_path
        self.verbose = verbose

    def start(self, question_list):
        """
        `question_list` list of questions to ask ChatGPT
        """
        asyncio.run(self.__start(question_list))

    async def __start(self, question_list):
        self.succeed = 0
        self.file_lock = asyncio.Lock()
        self.question_queue = queue.Queue()
        for question in question_list: self.question_queue.put(question)

        question_index = 0

        while self.succeed < len(question_list):
            tasks = []
            for _ in range(self.rate_limit):
                tasks.append(self.async_ask(self.question_queue.get(), question_index))
                question_index += 1 

            await asyncio.gather(*tasks)

            if self.succeed < len(question_list): time.sleep(60)

    async def log(self, response):
        await self.file_lock.acquire()

        with open(self.out_path, "a") as outfile:
            outfile.write(json.dump(response))
            outfile.write("\n")

        self.succeed += 1
        self.file_lock.release()

    async def async_ask(self, question, question_index):
        try:
            if self.verbose: print(f"[sleepyask] INFO | ID {question_index} | ASKING: {question}")

            payload = {"messages": [{"role": "user", "content": question}], **self.configs}
            response = await openai_async.chat_complete(payload=payload, api_key=self.api_key, timeout=self.timeout)
            
            if response.status_code != 200: 
                if self.verbose: print(f"[sleepyask] INFO | ID {question_index} | {response.status_code}")
                raise ValueError("Should be 200")

            await self.log(response.text)
        except: 
            if self.verbose: print(f"[sleepyask] INFO | ID {question_index} | ERROR")
            self.question_queue.put(question)