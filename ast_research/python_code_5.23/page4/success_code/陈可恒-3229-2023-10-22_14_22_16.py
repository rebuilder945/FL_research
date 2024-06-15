a = eval(input())
b = []
for x in range(len(a)):
    if a.count(a[x])==1:
        b.append(a[x])
if b == []:
    print('False')
else:
    b.sort()
    print(*b,sep=',')
