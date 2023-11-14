FROM python:3.10-alpine3.15

WORKDIR /usr/data
COPY ./requirements.txt .

COPY ./app/ app

RUN pip install -r requirements.txt
EXPOSE 8000/tcp
CMD ["uvicorn","app.main:app","--host", "0.0.0.0", "--port", "8000"]