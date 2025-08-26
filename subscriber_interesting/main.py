from fastapi import FastAPI
from kafka import KafkaConsumer
import json
import os
from datetime import datetime
from manager import MongoManager
import threading

app = FastAPI()

KAFKA_SERVERS = os.getenv("KAFKA_SERVERS", "localhost:9092")
TOPIC = "interesting"
COLLECTION_NAME = "interesting"

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_SERVERS,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='subscriber-group'
)

mongo_manager = MongoManager()

def run_consumer():
    for message in consumer:
        doc = message.value
        doc['timestamp'] = datetime.utcnow().isoformat()
        mongo_manager.insert_one(COLLECTION_NAME, doc)

@app.on_event("startup")
def startup_event():
    t = threading.Thread(target=run_consumer, daemon=True)
    t.start()

@app.get("/messages")
def get_messages():
    messages = mongo_manager.fetch_all(COLLECTION_NAME)
    return {"messages": messages}