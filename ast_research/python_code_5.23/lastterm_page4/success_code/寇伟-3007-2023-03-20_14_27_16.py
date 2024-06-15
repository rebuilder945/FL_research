ls1=eval(input())
ls=[]
for i in ls1:
    ls.append(int(i))
ls1=ls[:]
n,m=map(int,input().split(','))

for i in range(n,m):
    if ls[i]:
        del ls[i]
print(ls)
if ls==ls1:
    print('error')


