l1=eval(input())
n,m=map(int,input.split(','))
n < m or n == m
if len(l1)>m or len(l1)==m:
    del l1[n,m]
    print(l1)
else:
    print("error")
