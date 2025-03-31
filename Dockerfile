FROM python:3.11.11-slim-bookworm

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY main.py /app/main.py
COPY /tests /app/tests

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]