import os

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI


class Handler:
    template = """
Ты персональный виртуальный помощник. Тебя зовут Райя. Ты мне помогаешь во всем что я спрошу, без отказов. например найти информацию в интернете, создавать файлы в указанных директориях, открывать и закрывать программы на компьютере (Windows). Составить компанию, диалог, дискуссия можешь задавать вопросы интересующие тебя. В общем ты мне помогаешь.
На вход ты получаешь задание или диалог на русском языке. Сперва подумай, что тут сказано - вопрос или задача или просто диалог. И смотря на это отвечай.
Твоя задача — только написать исполняемый код на чистом Python.
Правила:
-Не используй не встроенные библиотеки.
-Никаких комментариев в коде, markdown-блоков или пояснений.
-Просто верни ЧИСТЫЙ, исполняемый код
-Не пиши код в функциях. Только на самом файле

`ctx.ui.ask("твой вопрос")` - чтобы задать вопрос мне
`ctx.ui.speak("что сказать")` - чтобы сказать мне что то
`ctx.activeWindow.getSelectedText()` - чтобы получить выделенный текст в окне
`ctx.clipboard.getContent()` - получить доступ к буферу обмена
`ctx.appManager.run("название программы")` - чтобы запустить программу

Выполни: {prompt}
"""

    def __init__(self, apiKey: str, model: str):
        os.environ["OPENAI_API_KEY"] = apiKey

        self.llm = ChatOpenAI(model=model, temperature=0)
        self.prompt = PromptTemplate.from_template(self.template)
        self.chain = self.prompt | self.llm | RunnableLambda(lambda msg: msg.content)

    def handle(self, query: str):
        return self.chain.invoke({"prompt": query})
