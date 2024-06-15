a=input()
d=[str(n) for n in a.split(',')]
b=eval(input())
c=[]
for x in range(len(d)):
    c.append([d[x],b[x]])
print(c)    
