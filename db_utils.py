from init import initial_db
from settings import MONGO_COL_NAME

mydb = initial_db()
mycol = mydb[MONGO_COL_NAME]

def add_uuid_to_db(uuid: str, message: str, timestamp: str ):
    my_dict = { "id": uuid, "text": message, "timestamp": timestamp }
    x = mycol.insert_one(my_dict)

def search_text_db(message: str):

    myquery = { '$or':[{'text':message},{'text': {'$regex':message}}]}
    dict_result = mycol.find(myquery)
    return dict_result