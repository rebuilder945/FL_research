ls=eval(input())
kong=[]
for x in ls:
    a=ls.count(x)
    if a==1:
        kong.append(x)
print(kong)
