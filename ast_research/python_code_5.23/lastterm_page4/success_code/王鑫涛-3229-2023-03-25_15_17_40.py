a =list(eval(input()))
a.sort()
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
p=str(b)
o = p[1:-1]
if len(b)==0:
    print('False')
else:
    print(o)
