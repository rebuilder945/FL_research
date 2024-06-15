a=eval(input())
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
b.sort(reverse=True)
if len(b)==0:
    print(False)
else:
    print(','.join(str(i) for i in b))


