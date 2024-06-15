a=eval(input())
b=[]
for i in a:
    if i==0:
        b.append(i)
        a.remove(i)
    else:
        pass
print(a+b)

