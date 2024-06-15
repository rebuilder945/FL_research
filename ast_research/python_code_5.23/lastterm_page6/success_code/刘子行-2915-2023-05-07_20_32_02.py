def flower(x):
    m=0
    a=[i for i in str(x)]
    sum=0
    for x in a:
        sum=sum+(int(x))**3
    if sum==int(x):
        m=1
    return m
n=eval(input())
a1=[]
for x in range(n+1):
    if flower(x):
        a1.append(x)
if a1==[]:
    print('none')
else:
    for x in a1:
        print(x)
