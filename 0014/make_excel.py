import json
from xlwt import *


wb = Workbook()
ws = wb.add_sheet('active_sheet')


with open('student.txt', 'r') as js:
    dict_data = json.load(js)

list_of_key = [a for a in dict_data]

list_all_day = []

for i in list_of_key:
    list_data = [i]
    for j in dict_data[i]:
        list_data.append(j)
    list_all_day.append(list_data)
for i, j in enumerate(list_all_day):
    for k, l in enumerate(j):
        ws.write(i, k, l)
# wb.('student.xslx')

