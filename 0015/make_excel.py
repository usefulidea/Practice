import xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet('active_sheet')
path = 'numbers.txt'

list_of_data = []
list_of_data_1 = []

with open(path, 'r') as f:
    for i in f.readlines():
        list_of_data.append(i.replace('[', '').replace(']', ''))
for i in list_of_data:
    list_of_data_1.append(i.strip().split(','))
list_of_data_1.pop(0)
list_of_data_1.pop(-1)
print(list_of_data_1)
for i, j in enumerate(list_of_data_1):
    for k, l in enumerate(j):
        ws.write(i, k, l)

wb.save('number.xls')

