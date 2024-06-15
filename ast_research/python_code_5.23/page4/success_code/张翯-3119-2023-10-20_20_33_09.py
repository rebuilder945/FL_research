lst=eval(input())
r=[]
for i in lst:
    if i not in r:
        r.append(i)
print(r)
