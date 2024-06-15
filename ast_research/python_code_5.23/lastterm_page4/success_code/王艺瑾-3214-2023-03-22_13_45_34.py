a=eval(input())
c=a.count(0)
b=[0]
while 0 in a:
    a.remove(0)
for i in range(c):
        a=a+b
print(a)   

