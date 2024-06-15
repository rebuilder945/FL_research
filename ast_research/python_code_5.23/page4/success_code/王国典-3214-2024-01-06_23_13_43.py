ls=eval(input())
kong1=[]
kong2=[]
for x in ls:
    if x!=0:
        kong1.append(x)
    if x==0:
        kong2.append(x)
print(kong1+kong2)
