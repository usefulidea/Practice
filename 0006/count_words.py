import os, re

path = "diaries"

list_dir = os.listdir(path)

dic = {'source': 0}
most_words = 'source'
for i in list_dir:
    with open(f"{path}/{i}", 'r') as f:
        for line in f.readlines():
            words = re.findall("[a-zA-Z]+'*-*[a-z][A-Z]*", line)
        for ff in words:
            if ff not in dic:
                dic[ff] = 1
            else:
                dic[ff] = dic[ff] + 1
                if dic[ff] > dic[most_words]:
                    most_words = ff
print(f"最多：{most_words}:{dic[most_words]}")

result = sorted(dic.items(), key=lambda x: x[1], reverse=True)
print(f"前三：{result[0][0]}:{result[0][1]}, {result[1][0]}:{result[1][1]}, {result[2][0]}:{result[2][1]}")
