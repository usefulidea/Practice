import os, re

path = 'sorce'
sum_tips = 0
sum_cod = 0
sum_empty = 0
code_list = os.listdir(path)
for i in code_list:
    with open(f"{path}/{i}", 'r') as f:
        for ff in f.readlines():
            if re.findall("\s#\s", ff):
                sum_tips += 1
            if re.findall("[a-zA-Z]", ff):
                sum_cod += 1
            if re.findall("^\n{1}", ff):
                sum_empty += 1

print(f"注释行数：{sum_tips}\n代码行数： {sum_cod}\n空行行数：{sum_empty}\n")
