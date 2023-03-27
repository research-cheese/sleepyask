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
from dotenv import load_dotenv
from sleepyask.openai import chat

load_dotenv()  # take environment variables from .env.

# Your ChatGPT authentication configs
config = {
	"organization": os.getenv('OPENAI_ORGANIZATION_1'),
	"api_key": os.getenv('OPENAI_API_KEY_1'),
	"count": 1
}

# List of authentication configs
configs = [config]

# List of questions you would like to ask ChatGPT
question_list = ['What is 1 + 1?', 'What is 1 + 2?', 'What is 1 + 3?']

# The filename in which you would like your responses to be stored.
# sleepyask will create this file for you. If you create it yourself, there might be some problems.
output_file_path = 'draw.json'  

# Run sleepy_ask
chat.ask(configs=configs,
           questions=question_list,
           output_file_path=output_file_path,
           verbose=True)
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/84760072/227817860-f4aef84b-9992-4ddd-a99d-019566cce0c5.png" width="900" />
</p>

### Parameters
`sleepyask.openai.ask` has the following parameters:
#### Required
- `configs` :: **(required)** - should be a list of dicts containing `organization` (your OpenAI organization ID), `api key` (your OpenAI api key) and the `count` (the number of instances to spin up for asking questions)
- `questions` :: **(required)** - should be a list of strings containing questions you would like to ask ChatGPT.
- `output_file_path` :: **(required)** - should be a valid file path where you would like your responses to be stored. sleepyask will create this file for you. If you create this file yourself, there might be some problems.

#### Optional
- `verbose` :: **(optional)** - a boolean which specifies whether or not sleepyask should print its progress to the console. It is `False` by default
- `model` :: **(optional)** - to specify which ChatGPT model to use. It is `"gpt-3.5-turbo"` by default
- `system_text` :: **(optional)** - to specify system text. It is `
- `temperature` :: **(optional)** - to specify how deterministic ChatGPT's responses are. Ranges from `0-2` where higher numbers represent increased randomness. It is `1` by default.
- `max_tokens` :: **(optional)** - to specify the maximum number of tokens in ChatGPT's response. This is `2048` by default

## 💬 Get involved
- 🐛 **Found a bug or interested in adding a feature?** - Create an [issue][issue]  
- 🤗 **Want to help?** - Create a pull-request!  

[issue]: https://github.com/hwelsters/sleepyask/issues
