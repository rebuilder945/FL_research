lst=eval(input())
b=[]
for i in lst:
    a=lst.count(i)
    if a <2 and i not in b:
        b.append(i)
        b.sort()
    print(b.split(","))
if b ==[]:
    print(False)

