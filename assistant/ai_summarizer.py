from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser

load_dotenv()


class AiSummarizer:
    def get_chapter_summary(self, text):
        output_parser = StrOutputParser()
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "You are a writer's assistant. You will help with summarising and collecting data from a novel."),
            ("user", " Summarise the lithuanian text, output just the summary. Don't include any intro."
                     " The text: {input}")
        ])
        chain = prompt | llm | output_parser
        summary = chain.invoke(input=text)

        return summary

    def get_characters(self, text):
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        list_output_parser = CommaSeparatedListOutputParser()
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a writer's assistant."),
            ("user",
             " Find all the characters mentioned in this lithuanian text. Return only their names in a comma separated list."
             " The text: {input}")
        ])

        chain = prompt | llm | list_output_parser
        characters = chain.invoke(input=text)

        return characters


    def describe_character(self, character_name, text):
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.6)
        output_parser = StrOutputParser()
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a writer's assistant. Output only once setence describing a psychical appearance of a character."),
            ("user",
             " Describe the character's {character} physical appearance in once sentence based on the first chapter they appear in: {chapter}. Write only in english")
        ])

        chain = prompt | llm | output_parser
        description = chain.invoke(input={"character": character_name, "chapter": text})

        return description

