FROM python:3.12

ARG EMBEDDING_MODEL_NAME

RUN pip install torch  --index-url https://download.pytorch.org/whl/cpu

RUN pip install sentence-transformers

COPY ./app_requirements.txt /

RUN pip install -r app_requirements.txt

# Download model using build-time ARG
RUN python -c "\
from sentence_transformers import SentenceTransformer; \
model_name = '${EMBEDDING_MODEL_NAME}'; \
print(f'Downloading model: {model_name}'); \
SentenceTransformer(model_name)"

COPY ./app /app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
