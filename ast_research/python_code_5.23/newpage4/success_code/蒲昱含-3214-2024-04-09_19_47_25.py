a=eval(input())
b=a.count(0)
c=[d for d in a if a!=0]+[0]*b
print(c)
