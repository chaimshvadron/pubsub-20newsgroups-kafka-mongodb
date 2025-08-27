FROM python:3.11-slim

WORKDIR /app

COPY . .
COPY data ./data

RUN pip install --no-cache-dir -r publisher/requirements.txt

CMD ["uvicorn", "publisher.main:app", "--host", "0.0.0.0", "--port", "8000"]