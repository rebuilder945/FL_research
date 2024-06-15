a=eval(input())
b=[]
while 0 in a:
    a.remove(0)
    b.append(0)
c=a+b
print(c)
