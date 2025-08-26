from fastapi import FastAPI
from kafka import KafkaProducer
import json
import os
import random


app = FastAPI()

KAFKA_SERVERS = os.getenv("KAFKA_SERVERS", "localhost:9092")
TOPICS = {
    "interesting": "interesting",
    "not_interesting": "not_interesting"
}

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def load_messages(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/publish")
def publish_messages():
    interesting_msgs = load_messages("../data/newsgroups_interesting.json")
    not_interesting_msgs = load_messages("../data/newsgroups_not_interesting.json")
    selected_interesting = random.sample(interesting_msgs, 20)
    selected_not_interesting = random.sample(not_interesting_msgs, 20)

    for msg in selected_interesting:
        producer.send(TOPICS["interesting"], msg)
    for msg in selected_not_interesting:
        producer.send(TOPICS["not_interesting"], msg)

    producer.flush()
    return {"status": "published", "count_interesting": len(selected_interesting), "count_not_interesting": len(selected_not_interesting)}