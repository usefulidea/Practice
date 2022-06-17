import json
import xlwt

path = 'city.txt'

with open('city.txt', 'r') as f:
    dict_city = json.load(f)

wb = xlwt.Workbook()
ws = wb.add_sheet("active_sheet")

list_of_key = [a for a in dict_city]

list_all_data = []

for i in list_of_key:
    list_data = [i, dict_city[i]]
    list_all_data.append(list_data)
for i, j in enumerate(list_all_data):
    for k, l in enumerate(j):
        ws.write(i, k, l)
wb.save('city.xslx')
