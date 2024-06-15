n1=eval(input())
n,m=eval(input())
if n-1>len(n1)or m-1>len(n1):
    print("error")
else:
    del n1[n:m]
    print(n1)
