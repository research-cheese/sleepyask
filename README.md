![image](https://user-images.githubusercontent.com/84760072/223039320-2eb3b41f-3981-448d-a899-52ee9cb63acd.png)

<p align="center">
  A small tool for automating collecting data from ChatGPT over long periods of time.
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/palette/macchiato.png" width="400" />
</p>

<p align="center">
	<a href="https://github.com/hwelsters/sleepyask/stargazers">
		<img alt="Stargazers" src="https://img.shields.io/github/stars/hwelsters/sleepyask?style=for-the-badge&logo=starship&color=C9CBFF&logoColor=D9E0EE&labelColor=302D41"></a>
	<a href="https://github.com/hwelsters/sleepyask/releases/latest">
		<img alt="Releases" src="https://img.shields.io/github/release/hwelsters/sleepyask.svg?style=for-the-badge&logo=github&color=F2CDCD&logoColor=D9E0EE&labelColor=302D41"/></a>
	<a href="https://github.com/hwelsters/sleepyask/issues">
		<img alt="Issues" src="https://img.shields.io/github/issues/hwelsters/sleepyask?style=for-the-badge&logo=gitbook&color=B5E8E0&logoColor=D9E0EE&labelColor=302D41"></a>
</p>

## What does it do?
ChatGPT currently limits the number of questions that users may ask per hour. The goal of this project is to allow users to just leave their computers on for extended periods of time to collect large amounts of responses from ChatGPT. There might not be a lot of practical use for this. Its main use is in research or data analysis.

## Install as a Python Library
```
pip install sleepyask
```

![image](https://user-images.githubusercontent.com/84760072/223040760-e440fd82-9fa0-4869-9ea0-7028373752ee.png)

## Documentation

### Authentication
You are required to provide an organization as well as an API Key  
`organization` - Your organization ID. Get it here: https://platform.openai.com/account/org-settings  
`api_key` - You create an API Key on OpenAI by. Get it here: https://platform.openai.com/account/api-keys
```
Clicking on your profile picture on the top-right > View API Keys > Create new secret key.  
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
```

## Get involved
- 🐛 **Found a bug or interested in adding a feature?** - Create an [issue][issue]  
- 🤗 **Want to help?** - Create a pull-request!  

## Credits
- I copied/stole [Catppuccin's](https://github.com/catppuccin) beautiful colors and README.

[issue]: https://github.com/hwelsters/sleepyask/issues
