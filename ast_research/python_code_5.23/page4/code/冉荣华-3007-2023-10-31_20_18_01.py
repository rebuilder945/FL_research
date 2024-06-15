l1=eval(input())
n,m=map(int,input.split(','))
n < m or n == m
if len(l1)>m or len(l1)==m:
    for x in range(n,m):
        del l1(x)
    print(l1)
else:
    print("error")
