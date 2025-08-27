class MongoDAL:
    def __init__(self, db=None):
        self.db = db

    def fetch_all(self, collection_name):
        collection = self.db[collection_name]
        documents = list(collection.find({}, {"_id": 0}))
        return documents

    def insert_one(self, collection_name, document):
        collection = self.db[collection_name]
        collection.insert_one(document)

    def ensure_collection(self, collection_name):
        if collection_name not in self.db.list_collection_names():
            self.db.create_collection(collection_name)
