a=eval(input())
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i) 
b.sort()
if len(b)>0:
    for i in b:
        c=",".jion(str(i))
        print(c)
else:
    print('False')
