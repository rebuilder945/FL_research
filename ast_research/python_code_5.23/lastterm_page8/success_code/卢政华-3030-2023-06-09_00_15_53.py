a=input().split(',')
b=input().split(',')
a=list(a)
b=list(b)
c=list[(zip (a,b))] 
c.sort(key=lambda x:x[1])
print(c)

