s=eval(input())
s.sort()
ls=[]
for i in s:
    if s.count(i)==1:
        ls.append(i)
if ls==[]:
    print('False')
else:
    print(*ls,sep=',')
