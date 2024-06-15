a=eval(input())
b=[]
for x in a:
    if x%(i for i in range(2,x))==0:
        b.append(x)
a.remove(b)
print(a)
