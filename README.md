<p align="center">
  <img src="https://user-images.githubusercontent.com/84760072/227816421-0b042248-21e6-4bdf-9f3d-c6172123d478.png" width=450/>
</p>

<p align="center">
  A small tool for automating collecting data from ChatGPT over long periods of time.
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/84760072/227807017-21bcda58-4e89-4470-bb8d-738e9269ccae.png" width="900" />
</p>

<p align="center">
	<a href="https://github.com/hwelsters/sleepyask/stargazers">
		<img alt="Stargazers" src="https://img.shields.io/github/stars/hwelsters/sleepyask?style=for-the-badge&logo=starship&color=f9e1cb&logoColor=ffffff&labelColor=342430"></a>
	<a href="https://github.com/hwelsters/sleepyask/releases/latest">
		<img alt="Releases" src="https://img.shields.io/github/release/hwelsters/sleepyask.svg?style=for-the-badge&logo=starship&color=f9e1cb&logoColor=ffffff&labelColor=342430"/></a>
	<a href="https://github.com/hwelsters/sleepyask/issues">
		<img alt="Issues" src="https://img.shields.io/github/issues/hwelsters/sleepyask?style=for-the-badge&logo=starship&color=f9e1cb&logoColor=ffffff&labelColor=342430"></a>
</p>

## What does it do?
ChatGPT currently limits the number of questions that users may ask per hour. The goal of this project is to allow users to just leave their computers on for extended periods of time to collect large amounts of responses from ChatGPT. There might not be a lot of practical use for this. Its main use is in research or data analysis.

## Installation
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
  <img src="https://user-images.githubusercontent.com/84760072/227807017-21bcda58-4e89-4470-bb8d-738e9269ccae.png" width="900" />
</p>

## Usage

### Authentication
You are required to provide an organization as well as an API Key  
`organization` - Your organization ID. Get it here: https://platform.openai.com/account/org-settings  
`api_key` - You create an API Key on OpenAI by. Get it here: https://platform.openai.com/account/api-keys
```bash
> Clicking on your profile picture on the top-right 
> View API Keys 
> Create new secret key.  
```
`count` - This specifies the number of workers to create for asking questions. You can have multiple workers asking questions in parallel.  
	
Sample config
```python
config = {
	"organization": "Your OpenAI organization",
	"api_key": "Your OpenAI api key",
	"count": 1 
}
```
### Sample code
```python
from sleepyask.openai import chat

# Your ChatGPT login information
config_1 = {
	"organization": "Your ChatGPT organization",
	"api_key": "Your ChatGPT api key",
	"count": 1
}

config_2 = {
	"organization": "Your ChatGPT organization",
	"api_key": "Your ChatGPT api key",
	"count": 1
}

configs = [config_1, config_2]

## List of questions you would like to ask ChatGPT
question_list = [
  'What is 1 + 1?',
  'What is 1 + 2?',
  'What is 1 + 3?'
]

# The filename in which you would like your responses to be stored.
# sleepyask will create this file for you. If you create it yourself, there might be some problems.
output_file_path = 'draw.json'  

# Run sleepy_ask
chat.ask(configs=configs,
           questions=question_list,
           output_file_path=output_file_path,
           verbose=True)

# chat.ask has the following optional parameters:
# verbose : bool = Whether or not sleepyask should print its prompts. It is False by default.
# model: str = The ChatGPT model to ask. This is "gpt-3.5-turbo" by default.
# system_text: str | None = System text to prime ChatGPT. This is None by default.
# temperature: float | None = Defines how non-deterministic ChatGPT is. Ranges from 0 - 2. Lower values are more deterministic. This is 1 by default
# max_tokens: int | None = Defines the maximum number of tokens in ChatGPT's response. This is 2048 by default.
```

## Get involved
- 🐛 **Found a bug or interested in adding a feature?** - Create an [issue][issue]  
- 🤗 **Want to help?** - Create a pull-request!  

[issue]: https://github.com/hwelsters/sleepyask/issues
