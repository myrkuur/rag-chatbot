FROM python:3.12

# Install dependencies
RUN pip install pysqlite3-binary

RUN pip install torch  --index-url https://download.pytorch.org/whl/cpu

COPY ./app_requirements.txt /

RUN pip install -r app_requirements.txt

COPY ./app /app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
