a=list(eval(input()))
n,m=eval(input())
b=a
if n < len(a):
    for i in range(m):
        b.append(a[n])
    print(b)   
else:
    print("error")
   
