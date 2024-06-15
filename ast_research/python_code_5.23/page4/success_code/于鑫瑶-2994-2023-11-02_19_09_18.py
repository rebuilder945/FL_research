a=list(input())
n,m=eval(input())
s=a[n]*m
a.append(s)
if n>len(a):
    print("error")
else:
    print(a)
