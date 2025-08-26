from publisher.kafka_configurations import get_producer_config

TOPICS = {
    "interesting": "interesting",
    "not_interesting": "not_interesting"
}

producer = get_producer_config()

def send_messages(topic, messages):
    for msg in messages:
        producer.send(topic, msg)
    producer.flush()
