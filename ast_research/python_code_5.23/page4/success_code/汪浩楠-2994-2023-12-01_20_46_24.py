a=list(eval(input()))
n,m=eval(input())
b=a[n]
if 0<=n<len(a):
    for i in range(m): 
        a.append(b)
    print(a)
else:
    print("error")


