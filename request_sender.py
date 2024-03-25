import os
from dotenv import load_dotenv

def create_new_thread(content: str, client, assistant):
  
  load_dotenv()
  CREATE_ASSISTANT_INSTRUCTIONS = os.getenv('CREATE_ASSISTANT_INSTRUCTIONS')

  thread = client.beta.threads.create()

  thread_message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=content,
  )

  run = client.beta.threads.runs.create(
    thread_id = thread.id,
    assistant_id = assistant.id,
    instructions = CREATE_ASSISTANT_INSTRUCTIONS
  )

  while run.status != "completed":
      keep_retrieving_run = client.beta.threads.runs.retrieve(
          thread_id=thread.id,
          run_id=run.id
      )
      if keep_retrieving_run.status == "completed":
          all_messages = client.beta.threads.messages.list(
              thread_id=thread.id
          )
          response =  all_messages.data[0].content[0].text.value
          return response
