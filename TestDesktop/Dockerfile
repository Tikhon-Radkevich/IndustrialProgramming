FROM python:3.11

RUN mkdir -p /app
RUN chmod 666 /app

RUN mkdir -p /app/cache
RUN chmod 666 /app/cache

WORKDIR app

COPY .. .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "main.py"]
