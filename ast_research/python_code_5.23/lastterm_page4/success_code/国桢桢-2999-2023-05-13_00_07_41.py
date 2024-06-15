l = input().split()
l2 =input().split()
n = int(l2[0])
m = int(l2[1])
if n < m:
    n,m = m,n
 #n>m
a = l.pop(n)
b = l.pop(m)
l.insert(m,a)
l.insert(n,b)
print(l)   
