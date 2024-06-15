a=eval(input())
a=list(a)
b=[]
x=0
for i in a:
    if i == 0:
        b.append(i)
        a.remove(i)
c=a+b
print(c)        




