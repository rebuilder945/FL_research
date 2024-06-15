a=eval(input())
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i) 
if len(b)>0:
    for i in b:
        print(i)
else:
    print('False')
