FROM python:3.12-alpine

COPY . /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN chmod +x writers_assistant.sh

ENTRYPOINT ["./writers_assistant.sh"]
