a=eval(input())
n=a.count(0)
c=[x for x in a if x !=0]
b=[0 for x in range(n)]
c.extend(b)
print(c)
