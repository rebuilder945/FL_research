a=list(eval(input()))
n,m=eval(input())
s=[]
b=len(a)
if m<=b-1:
    s.extend(a[0:n])
    s.extend(a[m:])
    print(s)
else:
    print("error")
