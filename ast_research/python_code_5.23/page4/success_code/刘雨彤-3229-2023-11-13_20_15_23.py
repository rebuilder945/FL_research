a=eval(input())
b=[]
for i in a:
    jishu=0
    if a.count(i)==1:
        b.append(i)
        jishu+=1
if jishu==0:
    print('False')
else:
    print(b.sort())
