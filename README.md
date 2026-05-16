# openai-chat
Calls the OpenAI API from a Node.js app. Uses system prompt, temperature adjustment, and logs token counts.

# Setup
The project is created using Python3.13. To run it perform the following steps:

## 1. Setup virtual env
```
python3.13 -m venv openai_venv
```

## 2. Activate the Environment
```
source openai_venv/bin/activate        
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
python3.13 src/chat.py
```
It will output a sample story
