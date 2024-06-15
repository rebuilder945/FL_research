a=list(input())
n,m=print()
n=eval(n)
m=eval(m)
s=a[n]*m
a.append(s)
if n>len(a):
    print("error")
else:
    print(a)
