import re

count = 0
with open('/Users/wangyu/Desktop/test.txt', 'r') as f:
    for line in f.readlines():
        list_num = re.findall("[a-zA-Z]+'*-*[a-zA-Z]*", line)
        count += len(list_num)
print(count)