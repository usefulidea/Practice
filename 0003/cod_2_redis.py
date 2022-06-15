import uuid

import redis
import os

r = redis.StrictRedis(host='localhost', port=6379)
with open('/Users/wangyu/Desktop/cod.txt', 'r') as cod_file:
    for i in range(len(cod_file.readlines())):
        r.set(f"cod_id{i}", str(uuid.uuid4()))
for i in range(20):
    print(r.get(f"cod_id{i}"))



