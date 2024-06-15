a=list(eval(input()))
n,m=eval(input())
b=[]
if n>=len(a):
    print("error")
else:
    for x in range(m):
        b.append(a[n])
    print(a+b)
