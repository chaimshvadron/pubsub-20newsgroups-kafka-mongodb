from subscriber_not_interesting.mongo import MongoDBConnection
from .dal import MongoDAL
    
class MongoManager:
    def __init__(self):
        self.db = None
        self.dal = None

    def fetch_all(self, collection_name):
        with MongoDBConnection() as conn:
            db = conn.get_db()
            dal = MongoDAL(db)
            dal.ensure_collection(collection_name)
            return dal.fetch_all(collection_name)

    def insert_one(self, collection_name, document):
        with MongoDBConnection() as conn:
            db = conn.get_db()
            dal = MongoDAL(db)
            dal.ensure_collection(collection_name)
            dal.insert_one(collection_name, document)
