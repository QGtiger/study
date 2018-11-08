import pymongo
import numpy as np
client = pymongo.MongoClient(host='localhost',port=27017)
client = client['mydb']
collection = client['student']

for _ in range(15):
    student={
        'id':np.random.randint(10,30),
        'name':''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz'),3)), #Ëæ»úÈ¡Ãû×Ö
        'age':np.random.randint(10,30),
        'gender': 'male' if np.random.randn()>0 else 'female'
    }
    collection.insert_one(student)


results = collection.find({'name':{'$regex':'^m.*'}})
for result in results:
    print(result['name'])

results = collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(2)
#print(results)
print(result['name'] for result in results)
for result in results:
    print(result['name'])

results =collection.delete_many({'age':{'$gte':25}})
print(results.deleted_count)