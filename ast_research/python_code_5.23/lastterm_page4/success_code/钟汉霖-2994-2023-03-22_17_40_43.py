a=list(eval(input()))
n,m=eval(input())
if n<0:
    n+=len(a)
if n>=len(a) or n<0:
    print("error")
else:
    for i in range(m):
       a.append(a[n])
    print(a)
