a=list(input())
b=[]
for x in range(len(a)):
    if a[x].count==1:
        b.append(a[x])
if len(b)>=1:
    print(b[0])
else:
    print('None')
