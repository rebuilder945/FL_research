num=eval(input())
a=num.count(0)
while num.count(0)>0:
    num.remove(0)
b=[0]*a
num=num+b
print(num)

