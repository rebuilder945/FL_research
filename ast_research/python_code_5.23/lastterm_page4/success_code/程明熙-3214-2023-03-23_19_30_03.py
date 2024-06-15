l=eval(input())
a=[]
b=l.count(0)
for i in l:
    if i!=0:
        a.append(i)
for i in range(0,b):
    a.append(0)
print(a)
