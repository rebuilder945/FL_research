a=list(eval(input()))
n,m=eval(input())
if n < len(a):
    x=a[n]
    for i in range(m):
        a.append(x)
    print(a) 
else:
    print("error")
   
