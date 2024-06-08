import logging
import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
import random
import string


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
                + "gender: " + gender + "image only without typography, be in the style of drawings, and be visually appealing"
            }
        ],
    )
    description = response.choices[0].message.content
    logging.info(description)

    response = client.images.generate(
        model="dall-e-3",
        prompt=description + "graphite drawing",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    return save_image_from_url(response.data[0].url)


def save_image_from_url(url):
    response = requests.get(url)
    file_name = generate_random_string(10) + ".jpg"
    file_path = "assistant/static/" + file_name
    with open(file_path, 'wb') as file:
        file.write(response.content)
    return file_name


def generate_random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
