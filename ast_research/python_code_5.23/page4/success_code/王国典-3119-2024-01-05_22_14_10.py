ls=eval(input())
kong=[]
for x in ls[::-1]:
    if x not in kong:
        kong.append(x)
kong1=kong[::-1]
print(kong1)

