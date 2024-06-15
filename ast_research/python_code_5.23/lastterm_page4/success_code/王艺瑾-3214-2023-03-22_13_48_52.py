a=eval(input())
c=a.count(0)
b=[0]*c
while 0 in a:
    a.remove(0)

print(a+b)   

