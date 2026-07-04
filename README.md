# lit.bot
lit.bot is a Python reading comprehension tool designed to help grade 4-8 students improve reading comprehension.
It prompts for the genre the student is interested in and then 
displays a paragraph for the student to read. It presents multiple choice questions for them to answer.
Finally, it provides feedback to the responses, suggests ways to improve, and statistics.

# Setup
The project is created using Python3.13. To run it perform the following steps:

## 1. Setup virtual env
```
python3.13 -m venv lit.bot_venv
```

## 2. Activate the Environment
```
source lit.bot_env/bin/activate        
```

## 3. Install the pip-tools 
Pip-tools is used to manage tracking of the packages. You can install it as
```
pip install pip-tools
```

## 4. Sync the packages
```
pip-sync requirements.txt
```

## 5. Update the .env file
Make a copy of `.env.sample` and rename it as `.env`. Add your OPENAI_API_KEY secret

# Run the project
After completing the setup, you should be able to run it by the command:
```
python3.13 src/read.py
```
It will output a sample story
