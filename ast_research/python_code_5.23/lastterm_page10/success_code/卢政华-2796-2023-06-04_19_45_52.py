a=input()
b=''
c=''
if not any(c.isdigit() for c in a):  # 判断是否含有数字字符
    print("No digits")
else:
    for i in a:
        if i.isdigit():
            b+=i
    else:
        if len(b)>len(c):
            c=b
        b=''
print(c)
