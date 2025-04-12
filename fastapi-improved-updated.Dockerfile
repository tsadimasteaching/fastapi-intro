FROM python:3.12.10-alpine3.21 as base

COPY ./requirements-updated.txt .

RUN pip install --no-cache-dir -r requirements-updated.txt

FROM python:3.12.10-alpine3.21 as build

# Copy the installed dependencies from the builder stage to the final image
COPY --from=base /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=base /usr/local/bin /usr/local/bin

FROM alpine:3.21
COPY --from=build /usr/local/lib/ /usr/local/lib/
COPY --from=build  /usr/local/bin/ /usr/local/bin/
COPY --from=build  /usr/lib/ /usr/lib/

WORKDIR /app
COPY . /app
RUN addgroup -S appuser && adduser -S appuser -G appuser  --home /app && \
    chown -R appuser:appuser /app

USER appuser:appuser
ENV PATH=$PATH:/app/.local/bin

EXPOSE 8000/tcp
CMD ["uvicorn","app.main:app","--host", "0.0.0.0", "--port", "8000"]   
