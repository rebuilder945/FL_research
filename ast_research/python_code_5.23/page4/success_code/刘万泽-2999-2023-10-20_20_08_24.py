a=eval(input())
n,m=eval(input())
t=a[n]
p=a[m]
M=t
N=p
a.insert(n,M)
a.pop(n)
a.insert(m,N)
a.pop(m)
print(a,'end:''')

