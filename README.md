![image](https://user-images.githubusercontent.com/84760072/221397091-5e8e5d8b-5f96-49d6-9005-212424ff8c50.png)
![image](https://user-images.githubusercontent.com/84760072/221397101-1df32e05-75d6-4a00-93d8-a90e8ba0e22f.png)

<p align="center">
  A small tool for automating collecting data from ChatGPT
</p>

## Install as a Python Library
```
pip install pyreason
```

## Sample code
Example usage:
```python
from sleepyask.chat import sleepy_ask

output_file_path = 'draw.json'  # The file path in which you would like your responses to be stored

config = {
  "email": "Your ChatGPT email",
  "password": "Your ChatGPT password"
}
question_list = [
  'What is 1 + 1?',
  'What is 1 + 2?',
  'What is 1 + 3?'
]
sleepy_ask(config=config,
           questions=question_list,
           output_file_path=output_file_path)
```
## Get involved
- 🐛 **Found a bug or interested in adding a feature?** - Create an [issue][issue]  

[issue]: https://github.com/hwelsters/sleepyask/issues
