a=eval(input())
ls=[]
for i in a:
    if a.count(i)==1 and ls.count(i)<1:
        ls.append(i)
ls.sort()
if len(ls)==0:
    print('False')
else:
    b = ','.join(str(i) for i in b)
    print(b)
         
