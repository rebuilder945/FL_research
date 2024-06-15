lst=eval(input())
b=[]
for i in lst:
    a=lst.count(i)
    if a <2 and i not in b:
        b.append(i)
        b.sort()
        c=int("".join(list(map(str,b))))
        print(c)
if b ==[]:
    print(False)

