a=input()
n,m=eval(input().split(" "))
a=a.split(" ")
b=a[n]
a.insert(m,b)
c=a[m+1]
del a[m+1]
a.insert(n,c)

