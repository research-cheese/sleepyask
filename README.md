<p align="center">
  <img src="https://user-images.githubusercontent.com/84760072/227817729-098182f3-6916-48d8-b17a-4e4126ddd245.png" width=450/>
</p>

<p align="center">
  A small tool for collecting data from ChatGPT over long periods of time.
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/84760072/227817860-f4aef84b-9992-4ddd-a99d-019566cce0c5.png" width="900" />
</p>

<p align="center">
	<a href="https://github.com/hwelsters/sleepyask/stargazers">
		<img alt="Stargazers" src="https://img.shields.io/github/stars/hwelsters/sleepyask?style=for-the-badge&logo=starship&color=f9e1cb&logoColor=ffffff&labelColor=5f8872"></a>
	<a href="https://github.com/hwelsters/sleepyask/releases/latest">
		<img alt="Releases" src="https://img.shields.io/github/release/hwelsters/sleepyask.svg?style=for-the-badge&logo=starship&color=f9e1cb&logoColor=ffffff&labelColor=5f8872"/></a>
	<a href="https://github.com/hwelsters/sleepyask/issues">
		<img alt="Issues" src="https://img.shields.io/github/issues/hwelsters/sleepyask?style=for-the-badge&logo=starship&color=f9e1cb&logoColor=ffffff&labelColor=5f8872"></a>
</p>

## 💬 What does it do?
ChatGPT rate limits the number of questions users may ask. The goal of this project is to allow users to just leave their computers on for extended periods of time to collect large amounts of responses from ChatGPT. Contributions are welcome! 🤗

## 💬 Installation
To install sleepyask, do one of the following:
```bash
> pip install sleepyask
> py -m pip install sleepyask
> python -m pip install sleepyask
```
This project also depends on the following packages
```bash
> openai
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/84760072/227817860-f4aef84b-9992-4ddd-a99d-019566cce0c5.png" width="900" />
</p>

## 💬 Usage

### Authentication
You are required to provide an organization as well as an API Key  
- `organization` - Your OpenAI organization ID. Get it here: https://platform.openai.com/account/org-settings  
- `api_key` - You OpenAI API Key. To get it:
```bash
> Go to https://platform.openai.com/account/api-keys
> Login (if it is required)
> Click on your profile picture on the top-right 
> View API Keys 
> Create new secret key.  
```
- `count` - This specifies the number of workers to create for asking questions. You can have multiple workers asking questions in parallel.  
	
### Sample code
It is recommended that you do not store your user credentials directly in your code. Instead, use something like `python-dotenv` to store your credentials in another file.
```python
import os
from dotenv import load_dotenv

from sleepyask.chat import Sleepyask

load_dotenv()  # take environment variables from .env.

TIMEOUT = 10000
RETRY_TIME = 5
RATE_LIMIT = 5
API_KEY = os.getenv('OPENAI_API_KEY')

# Index should be unique as it will be used to avoid repeat questions
QUESTION_LIST = [
	{'index': 1, 'text': 'What is 1 + 1?'},
	{'index': 2, 'text': 'What is 1 + 2?'},
	{'index': 3, 'text': 'What is 1 + 3?'}
]
OUT_PATH = 'output.jsonl'


CONFIGS = { "model": "gpt-3.5-turbo", "n": 10, "temperature": 0.7}
sleepyask = Sleepyask(configs=CONFIGS, 
                      rate_limit=RATE_LIMIT,
                      api_key=API_KEY, 
                      timeout=TIMEOUT, 
                      verbose=True,
                      retry_time=RETRY_TIME)

sleepyask.start(question_list=QUESTION, out_path=OUT_PATH)
```

## 💬 Get involved
- 🐛 **Found a bug or interested in adding a feature?** - Create an [issue][issue]  
- 🤗 **Want to help?** - Create a pull-request!  

[issue]: https://github.com/hwelsters/sleepyask/issues
