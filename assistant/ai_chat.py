import os
import openai

class ChatApp:
    messages = []

    def __init__(self):
        # Setting the API key to use the OpenAI API
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.messages.append(
            {"role": "system",
             "content": "You are a beta reader for a novel. The author will asked you a question expecting feedback:"},
        )

    def chat(self, message):
        self.messages.append({"role": "user", "content": message})
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        #todo add chat history to database
        #self.messages.append({"role": "assistant", "content": response["choices"][0]["message"].content})

        return response.choices[0].message.content
