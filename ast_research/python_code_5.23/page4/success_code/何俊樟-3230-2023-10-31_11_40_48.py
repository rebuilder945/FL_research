a=eval(input())
a.sort()
a.reverse()
e=str(a[0])
for x in range(len(a)-1):
    d=a[x+1]
    e=e+d
print(e)
    
    
    
