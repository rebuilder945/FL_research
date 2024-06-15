lst=eval(input())
res=[]
for i in lst:
    if i not in res:
        res.append(i)
print(res)

