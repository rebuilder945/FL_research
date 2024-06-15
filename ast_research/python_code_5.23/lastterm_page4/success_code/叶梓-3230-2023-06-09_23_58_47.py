ls=eval(input())
ls.sort()
ls.reverse()
text=''
for i in ls:         #列表转换为字符串
    text=text+str(i)
if int(text)==0:
    print(0)
else:
    print(text)
