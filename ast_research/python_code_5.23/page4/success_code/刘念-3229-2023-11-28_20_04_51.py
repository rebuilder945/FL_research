a = eval(input())
b=[]
for i in a:
    if a.count(i)==1:
        i = str(i)
        b.append(i)
if b==[]:
    print('False')
else:
    b.sort()
    m = ','.join(b)
    print(m)








    

