import os
import openai
from request_sender import create_new_thread

with open('reviews.txt', 'r', encoding='utf-8') as f:
    data = f.read().replace("\n", " ").split("*")

openai.api_key = "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"
client = openai.OpenAI(api_key=openai.api_key)


assistant = client.beta.assistants.retrieve(
    assistant_id="asst_e8EaO1weVkeACIGjzCNoLNHA"
)

data = [i for i in data if i]
responses = []
for user_review in data:
    responses.append(create_new_thread(content=user_review, assistant=assistant, client=client) + "\n\n")

with open('responses.txt', 'w+', encoding='utf-8') as f:
    f.writelines(responses[:-1])