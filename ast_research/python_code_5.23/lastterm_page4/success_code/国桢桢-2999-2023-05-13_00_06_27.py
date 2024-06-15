l = input().split()
l2 =input().split()
n = l2[0]
m = l2[1]
if n < m:
    n,m = m,n
 #n>m
a = l.pop(n)
b = l.pop(m)
l.insert(m,a)
l.insert(n,b)
print(l)   
