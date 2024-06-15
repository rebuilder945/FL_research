a=list(eval(input()))
n,m=eval(input())
x=a[n]
if n < len(a):
    for i in range(m):
        a.append(x)
    print(a) 
else:
    print("error")
   
