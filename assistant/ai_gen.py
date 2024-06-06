import logging
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def load_client():
    return OpenAI(
        # This is the default and can be omitted
        api_key=os.getenv("OPENAI_API_KEY"),
    )

def get_portrait(age, description, novel_genre, gender):
    client = load_client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "assistant",
                "content": "Please create a short description for image generation of a novel character:"
               + "age: " + str(age) + "description: " + description + " novel genre: " + novel_genre
                + "gender: " + gender +
                "Specify that the image should be a portrait of the character and it should contain no text. It should be in the style of a drawing."
            }
        ],
    )
    description = response.choices[0].message.content
    logging.error(description)

    response = client.images.generate(
        model="dall-e-3",
        prompt=description,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    return response.data[0].url


#print(get_portrait(20, "dark hair and blue eyes", "fantasy", "male"))