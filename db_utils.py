from init import initial_db
from settings import MONGO_COL_NAME

mydb = initial_db()
mycol = mydb[MONGO_COL_NAME]

def add_uuid_to_db(uuid: str, message: str, timestamp: str ):
    my_dict = { "id": uuid, "text": message, "timestamp": timestamp }
    x = mycol.insert_one(my_dict)

def search_text_db(message: str):

    myquery = { '$or':[{'text':message},{'text': {'$regex':message}}]}
    return list(mycol.find(myquery, { "_id": 0, "id": 1, "text": 1, "timestamp": 1 }))


if __name__ == "__main__":
    search_text_db('sag')

    