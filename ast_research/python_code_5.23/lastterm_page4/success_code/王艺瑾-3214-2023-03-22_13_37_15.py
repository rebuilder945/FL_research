a=eval(input())
c=a.count(0)
b=[0]*c
for i in a:
    if i==0:
        c=a.remove(i)
print(a+b)
        

