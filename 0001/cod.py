import random

import uuid

for i in range(0, 20):
    cod = uuid.uuid4()

    with open("/Users/wangyu/Desktop/cod.txt", 'a') as cod_file:
        cod_file.write(str(cod) + "\n")

