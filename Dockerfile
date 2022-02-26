FROM python:3.9.10-slim-buster

ENV PIP_NO_CACHE_DIR=1

RUN pip install tensorflow-cpu
RUN pip install FastAPI
RUN pip install scikit-learn
RUN pip install uvicorn
RUN pip install TurkishStemmer

WORKDIR /app/

COPY ./main.py .
COPY Models Models

EXPOSE 10001

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10001"]
