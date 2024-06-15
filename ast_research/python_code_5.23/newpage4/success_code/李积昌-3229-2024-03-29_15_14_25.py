a=eval(input())
b=[]
for i in a :

    if i not in b :
        c=i
        a.remove(i)
        b.append(c)
for x in b:
    if x in a:
        b.append(x)
if i==[]:
    print(False)
else:
    b.sort()
    print(int(b))
