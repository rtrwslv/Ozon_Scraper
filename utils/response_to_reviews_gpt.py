import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
from utils.request_sender import create_new_thread
import httpx

def pure_magic(request_text):
    load_dotenv()
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    PROXY_URL = os.getenv('PROXY_URL')
    
    proxies = {
        'http://': PROXY_URL,
        'https://': PROXY_URL
    }
    
    session = requests.Session()
    session.proxies = proxies

    client = OpenAI(http_client=httpx.Client(proxies=proxies))
    client.api_key = OPENAI_API_KEY

    assistant = client.beta.assistants.retrieve(
        assistant_id="asst_e8EaO1weVkeACIGjzCNoLNHA"
    )

    response = ""
    response += create_new_thread(content=request_text, assistant=assistant, client=client)
    
    return response