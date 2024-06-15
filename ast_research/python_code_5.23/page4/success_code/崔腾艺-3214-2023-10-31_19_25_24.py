a=eval(input())
b=a.count(0)
c=[]
for x in range(b):
    a.remove(0)
    c.append(0)
print(a+c)
