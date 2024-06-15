#删除不要与遍历操作同时进行，否则会导致混乱
a=list(eval(input()))
"""for i in a:
    b=a.count(i)
    if b==1:
        continue
    else :
        for x in range(0,b-1):
            a.remove(i)
以上为错误操作警惕
"""
c=[]
for i in a:
    b=a.count(i)
    if b==1:
        c.append(a[i])
    else:
        if not i in c:
            c.append(i)
print(c)        
