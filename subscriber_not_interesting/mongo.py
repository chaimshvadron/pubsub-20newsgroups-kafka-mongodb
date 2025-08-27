import os
from pymongo import MongoClient
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

class MongoDBConnection:
    def __init__(self):
        self.connection_string = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        self.db_name = os.getenv("MONGODB_DBNAME", "newsgroups")
        self.client = None
        self.db = None

    def __enter__(self):
        self.client = MongoClient(self.connection_string)
        self.db = self.client[self.db_name]
        print(f"Connected to MongoDB, database: {self.db_name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")

    def get_db(self):
        return self.db
