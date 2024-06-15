lis=eval(input())
n=lis.count(0)
if lis.count(0)>0:
    while lis.count(0)>0:
        lis.remove(0)
for x in range(n):
    lis.append(0)
print(lis)

