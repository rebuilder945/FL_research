a=list(range(1,10,2))+list(range(12,19,2))+list(range(19,28,2))+list(range(30,37,2))
c=list(range(1,37))
b=[]
for i in c:
    if i not in a:
        b.append(i)
x=eval(input())
if x in a:
    print('red')
elif x in b:
    print('black')
elif x==0:
    print('green')
else:
    print('error')

