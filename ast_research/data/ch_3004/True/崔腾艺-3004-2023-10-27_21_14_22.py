a=eval(input())
b=[]
for x in a:
    if x==2:
        b.append(2)
    elif x==3:
        b.append(3)
    elif x!=1 and x%2!=0 and x%3!=0:
        b.append(x)
    else:
        pass
print(b)
