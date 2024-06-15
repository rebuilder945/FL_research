a=eval(input())
b=[]
for i in a:
    if i==0:
        a.remove(i)
        b.append(i)
a=a+b
print(a)
