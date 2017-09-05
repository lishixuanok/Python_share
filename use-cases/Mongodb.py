import pymongo

# pymongo document
# https://api.mongodb.com/python/current/tutorial.html

devMongo = pymongo.MongoClient(host='your host', tz_aware=True)
user_table = devMongo['test']['appactivate_copy']


def delete(doc_id):
    user_table.remove({"_id": doc_id}, {'justOne': True})


def find_one(doc_id):
    data = user_table.find_one(filter={"_id": doc_id})
    return data


def insert(document):
    user_table.insert_one(document)


def update(doc_id, document):
    user_table.update_one(filter={"_id": doc_id}, update={"$set": document})


if __name__ == '__main__':
    print(find_one(doc_id='861487035927752'))
