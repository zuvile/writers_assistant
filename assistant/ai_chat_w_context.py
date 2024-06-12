from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
import csv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser

load_dotenv()


def summarise(novel_id):
    db = SQLDatabase.from_uri("sqlite:///db.sqlite3")

    chapter_ids = get_chapter_ids()
    summaries = []
    output_parser = StrOutputParser()

    for chapter_id in chapter_ids:
        print(chapter_id)

        chapter_text_str = str(
            db.run(f"SELECT text FROM assistant_paragraph WHERE novel_id={novel_id} AND chapter_id={chapter_id};"))
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a writer's assistant. You will help with summarising and collecting data from a novel."),
            ("user", " Summarise the lithuanian text, output just the summary. Don't include any intro."
                     " The text: {input}")
        ])
        chain = prompt | llm | output_parser
        summary = chain.invoke(input=chapter_text_str)

        summaries.append(summary)

        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a writer's assistant. You will help with summarising and collecting data from a novel."),
            ("user", " Find all the characters mentioned in this lithuanian text. Return only their names in a comma separated list."
                     " The text: {input}")
        ])

        list_output_parser = CommaSeparatedListOutputParser()
        chain = prompt | llm | list_output_parser
        characters = chain.invoke(input=chapter_text_str)

        print("Writing to csv file")
        with open('summaries.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([chapter_id, summary, characters])


def get_chapter_ids():

    return [608, 609]
    # return [607,
    #         608,
    #         609,
    #         610,
    #         611,
    #         612,
    #         613,
    #         614,
    #         615,
    #         616,
    #         617,
    #         618,
    #         619,
    #         620,
    #         621,
    #         622,
    #         623,
    #         624,
    #         625,
    #         626,
    #         627,
    #         628,
    #         629,
    #         630,
    #         631,
    #         632,
    #         633,
    #         634,
    #         635,
    #         636,
    #         637,
    #         638,
    #         639,
    #         640,
    #         641,
    #         642,
    #         643,
    #         644,
    #         645,
    #         646,
    #         647,
    #         648,
    #         649,
    #         650,
    #         651,
    #         652,
    #         653,
    #         654,
    #         655,
    #         656,
    #         657,
    #         658,
    #         659,
    #         660,
    #         661,
    #         662,
    #         ]


def main():
    summarise(4)


if __name__ == '__main__':
    main()
