a=list(input())
f=True
for i in a:
    if a.count(i)==1:
        f=False
        print(i)
        break
if f:
    print('None')
