a=eval(input())
b=len(a)
a.sort()
c=0
j=0
for x in a:
    d=x*(10**j)
    j=j+1
    c=c+d
print(c)
    
