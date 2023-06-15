from pymongo import MongoClient

array = [['dfdfdf', 'dhghfg'], ['sdfsdffll', 'tertere'], 'rew9ruwygg']

class MongoDB:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/GTD')
        self.db = self.client['GTD']
        self.collections = self.db['GTD_bot']

    def add_user(self, telegram_id):
        user = {
            "telegram_id": telegram_id,
            "list_of_quest_and_name_of_lists": 0,
            "basket": 0,
            "list_of_GTD_lists": 0
        }

        return self.collections.insert_one(user)
    
    def check_user_on_db(self, telegram_id):
        if self.collections.find_one({"telegram_id": telegram_id}) is None:
            return False
        else:
            return True
        
    def add_quests(self, telegram_id, array_of_quests_and_name_of_list):
        return self.collections.update_one({"telegram_id": telegram_id}, {"$set": {"list_of_quest_and_name_of_lists": array_of_quests_and_name_of_list}})

    def add_list_of_lists(self, telegram_id, array_of_quests_and_name_of_list):
        list_of_lists = []
        for i in array_of_quests_and_name_of_list:
            if type(i)==list:
                list_of_lists.append(i[1])
            else:
                list_of_lists.append(i)
        return self.collections.update_one({"telegram_id": telegram_id}, {"$set": {"list_of_GTD_lists": list_of_lists}})
    


DB = MongoDB()
DB.add_list_of_lists(228, array)