import os
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from .models import Chapter


class ChatApp:
    messages = []

    def __init__(self, novel_id):
        summaries = Chapter.objects.filter(novel_id=novel_id).values_list('summary', flat=True)
        output_parser = StrOutputParser()
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "You are a beta reader. You will read all the book and will answer questions about the plot, characters, etc."),
            ("user", " Here are all of the chapter summaries: {input}. Get ready to answer questions about the book.")
        ])
        chain = prompt | llm | output_parser
        response = chain.invoke(input=summaries)



    def chat(self, message):
        self.messages.append({"role": "user", "content": message})
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        # todo add chat history to database
        # self.messages.append({"role": "assistant", "content": response["choices"][0]["message"].content})

        return response.choices[0].message.content
