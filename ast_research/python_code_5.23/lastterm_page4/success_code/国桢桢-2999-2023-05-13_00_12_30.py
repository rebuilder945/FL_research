l = input().split()
l2 =input().split()
n = int(l2[0])
m = int(l2[1])
if n <0:
    n = len(l)+n
if m < 0:
    m = len(l)+m
if n < m and n>0:
    n,m = m,n
 #n>m
a = l.pop(n)
b = l.pop(m)
l.insert(m,a)
l.insert(n,b)
print(l)   
