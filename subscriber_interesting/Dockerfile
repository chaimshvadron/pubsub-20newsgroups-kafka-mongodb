FROM python:3.11-slim

WORKDIR /app

COPY ./subscriber_interesting/requirements.txt ./requirements.txt
COPY ./subscriber_interesting ./subscriber_interesting

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "subscriber_interesting.main:app", "--host", "0.0.0.0", "--port", "8000"]
