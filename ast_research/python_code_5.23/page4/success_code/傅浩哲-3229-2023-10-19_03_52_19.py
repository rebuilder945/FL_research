a=eval(input())
a.sort(reverse=False)
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
if b==[]:
    print('False')
else:
    s=','.join(str(x) for x in b)
    print(s)
