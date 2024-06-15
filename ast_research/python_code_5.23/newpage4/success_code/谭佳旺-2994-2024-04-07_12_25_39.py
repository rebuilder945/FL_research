lis1 =input().split(',')
a,b =input().split(',')
a=int(a)
b=int(b)
for i in range(b):
    lis2=lis1[a]
    lis1.append(lis2)
print(lis1)
