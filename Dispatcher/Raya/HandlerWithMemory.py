import os

import openai
from langchain_openai import ChatOpenAI

from Core.Handler import AbstractHandler


class Handler(AbstractHandler):
    def __init__(self, apiKey: str, model: str):
        os.environ["OPENAI_API_KEY"] = apiKey
        self.api_key = apiKey
        self.model = model
        self.assistant_id = 'asst_6oRFNaNScY1tlmpnzCWqvVD9'

        openai.api_key = self.api_key

        self.thread = openai.beta.threads.create()

        self.llm = ChatOpenAI(model=model, temperature=0)

    def handle(self, query: str) -> str:
        openai.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=query
        )

        run = openai.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant_id
        )

        import time

        while True:
            status = openai.beta.threads.runs.retrieve(thread_id=self.thread.id, run_id=run.id)

            if status.status == "completed":
                break

            time.sleep(0.5)

        messages = openai.beta.threads.messages.list(thread_id=self.thread.id)
        for msg in reversed(messages.data):
            if msg.role == "assistant":
                return msg.content[0].text.value

        return "Нет ответа от ассистента."
