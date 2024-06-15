ls=eval(input())
a=max(ls)
b=min(ls)
c=[]
for x in ls:
    if x!=a and x!=b:
        c.append(x)
print(c)
