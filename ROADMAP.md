![image](https://user-images.githubusercontent.com/84760072/221511635-fbcc8d46-a224-445b-a358-2290d314c300.png)

<p align="center">
  📋 Things to do:
</p>

[❌] **Certain people are currently using multiple ChatGPT accounts to collect data.** If it is possible, we can make something which allows multiple accounts to chip away at the question set together. One option is to make accounts take turns asking questions. However, this is not preferrable. We would prefer for multiple accounts to be asking questions at the exact same time.   
One idea I currently have in mind is to have multiple accounts share a single mutex which keeps track of the current question number.
- We need some way to handle questions that fail to be answered, so these will be logged and retried at a later time. 
