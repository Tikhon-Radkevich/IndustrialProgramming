FROM python:3.11

RUN mkdir IP

WORKDIR IP

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "main.py"]

