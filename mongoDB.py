from pymongo import MongoClient

class MongoDB:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/GTD')
        self.db = self.client['GTD']
        self.collections = self.db['GTD_bot']

    def add_user(self, telegram_id):
        user = {
            "telegram_id": telegram_id,
            "list_of_GTD_lists": 0
        }

        return self.collections.insert_one(user)
    

DB = MongoDB()
DB.add_user(228)