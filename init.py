import pymongo

import settings


def initial_db():
    client = pymongo.MongoClient(settings.MONGO_URL)
    return client[settings.MONGO_DB_NAME]
