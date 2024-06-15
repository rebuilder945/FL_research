import re 
s = input("输入一个字符串：")
ls = re.findall(r"\d+", s)
if ls:
    ss = ls[0]
    for i in ls:
        if len(i) >= len(ss):
            ss = i
    print(ss)
else:
    print("No digits")
