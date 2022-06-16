input_city = input("输入一个词： ")

list_alread_words = []
list_input = []

with open('filtered_word.txt', 'r') as f:
    line = f.readlines()
    for i in line:
        list_alread_words.append(i.strip())
if input_city in list_alread_words:
    for i in input_city:
        list_input.append(i)
    mark_num = len(input_city) * '*'
    print(mark_num + ' is a good city')
else:
    print(f"{input_city} is a good city")
