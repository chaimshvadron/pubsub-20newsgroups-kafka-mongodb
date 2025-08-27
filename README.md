# pubsub-20newsgroups-kafka-mongodb

## Project Description
A Pub/Sub system that classifies messages from the 20Newsgroups dataset using Kafka and stores them in MongoDB by category (interesting / not interesting). Each service runs in a separate container.

## How to Run

1. Make sure Docker is installed on your machine.
2. In the project root directory, run:

```
docker-compose up --build
```

3. The services will start automatically:
   - Publisher: http://localhost:8001
   - Subscriber Interesting: http://localhost:8002
   - Subscriber Not Interesting: http://localhost:8003
   - MongoDB: localhost:27017
   - Kafka: localhost:9092

4. You can test each API using a browser, curl, or Postman.

## Notes
- Each container communicates with Kafka and MongoDB using service names (kafka, mongo).
- Dockerfile and docker-compose.yml are configured for all services.
- Update requirements.txt files according to your dependencies.
