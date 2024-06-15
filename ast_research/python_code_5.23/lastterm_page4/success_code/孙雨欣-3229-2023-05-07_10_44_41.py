ls1=eval(input())
ls2=[]
for i in ls1:
    if ls1.count(i)==1:
        ls2.append(i)
if ls2==[]:
    print('False')
else:
    print(*ls2,sep=',')
