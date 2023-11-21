FROM python:3.10-alpine3.15

WORKDIR /usr/data
COPY ./requirements.txt .

COPY ./app/ app

RUN addgroup -S appuser && adduser -S appuser -G appuser -h /usr/data

RUN pip install -r requirements.txt

RUN chown -R appuser:appuser /usr/data

USER appuser:appuser


EXPOSE 8000/tcp
CMD ["uvicorn","app.main:app","--host", "0.0.0.0", "--port", "8000"]