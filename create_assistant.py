import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
THREAD_RUN_INSTRUCTIONS = os.getenv('THREAD_RUN_INSTRUCTIONS')

client = OpenAI()
OpenAI.api_key = OPENAI_API_KEY

assistant = client.beta.assistants.create(
    model="gpt-3.5-turbo",
    instructions = THREAD_RUN_INSTRUCTIONS ,
    name="Магазин",
)