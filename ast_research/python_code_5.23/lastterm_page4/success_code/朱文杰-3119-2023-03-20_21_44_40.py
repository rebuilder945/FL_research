lst=eval(input())
r=[]
for x in lst[::-1]:
    if x in lst and not x in r:
        r.insert(0,x)
print(r)
