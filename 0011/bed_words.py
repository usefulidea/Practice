
user_input = input("输入一个词   ")

list_check = []
with open('filtered_word.txt', 'r') as f:
    line = f.readlines()
    for i in line:
        list_check.append(i.strip())
if user_input in list_check:
    print("Freedom")
else:
    print("Human Rights")