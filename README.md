![image](https://user-images.githubusercontent.com/84760072/221397091-5e8e5d8b-5f96-49d6-9005-212424ff8c50.png)
![image](https://user-images.githubusercontent.com/84760072/221397101-1df32e05-75d6-4a00-93d8-a90e8ba0e22f.png)

<p align="center">
  A small tool for automating collecting data from ChatGPT
</p>

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
- 🐛 **Found a bug?** - Create an [issue][issue]  
- ⚙️ **Interested in adding a feature?** - Check out the [project roadmap](ROADMAP.md) or suggest your own changes by creating an [issue][issue]   
- 📖 **Can we improve the documentation?** - Even pull requests for small changes can be helpful. Feel free to change the [documentation][docs]!  
- 😵 **See something wrong with the dataset?** - While our dataset may be accurate most of the time, we make the assumption that the preexisting datasets have the correct working and that the questions use only distinct numbers.

