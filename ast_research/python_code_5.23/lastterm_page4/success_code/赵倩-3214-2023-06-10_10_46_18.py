a=eval(input())
l=[0]
b=a.count(0)
for i in range(b):
    a.remove(0)
l=l*b
a=a+l
print(a)






