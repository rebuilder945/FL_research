d=input()
a=d.split(',')
b=eval(input())
c=[]
for x in range(0,len(b)):
    results=[a[x],b[x]]
    c.append(results)
print(c)
