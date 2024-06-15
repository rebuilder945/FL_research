lst=eval(input())
b=[]
for i in lst:
    a=lst.count(i)
    if a >=2 and i not in b:
        b.append(i)
    elif b==[]:
        print(False)
b.sort()
print(b)
