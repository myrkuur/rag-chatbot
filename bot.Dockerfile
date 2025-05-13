FROM python:3.10-slim-bullseye

COPY ./bot_requirements.txt /

RUN pip install -r bot_requirements.txt

COPY ./bot.py /

CMD ["python", "bot.py"]