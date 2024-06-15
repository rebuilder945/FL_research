ls=eval(input())
ls1=[]
for x in ls:
    if x in ls1:
        continue
    else:
        ls1.append(x)
print(ls1)
