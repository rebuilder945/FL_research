a =list(eval(input()))
a.sort()
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
p=''.join(b)
if len(b)==0:
    print('False')
else:
    print(b)
