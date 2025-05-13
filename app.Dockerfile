FROM python:3.10-slim-bullseye

COPY ./app_requirements.txt /

RUN pip install -r app_requirements.txt

COPY ./app /

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
