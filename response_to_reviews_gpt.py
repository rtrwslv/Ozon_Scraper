import os
from dotenv import load_dotenv
from openai import OpenAI
from request_sender import create_new_thread

with open('reviews.txt', 'r', encoding='utf-8') as f:
    data = f.read().replace("\n", " ").split("*")

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI()
OpenAI.api_key = OPENAI_API_KEY

assistant = client.beta.assistants.retrieve(
    assistant_id="asst_e8EaO1weVkeACIGjzCNoLNHA"
)

data = [i for i in data if i]
responses = []
for user_review in data:
    responses.append(create_new_thread(content=user_review, assistant=assistant, client=client) + "\n\n")

with open('responses.txt', 'w+', encoding='utf-8') as f:
    f.writelines(responses[:-1])