lis=eval(input())
n,m=input().split(",")
n=int(n)
m=int(m)
if n>len(lis)-1 or m>len(lis)-1:
    print('error')
else:
    for i in range(n,m):
        lis.pop(i)
    print(lis)
