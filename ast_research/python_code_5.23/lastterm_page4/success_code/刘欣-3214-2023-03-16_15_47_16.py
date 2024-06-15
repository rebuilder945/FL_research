ls=eval(input())
for i in range(0,len(ls)):
    if ls[i]==0:
        a=ls.pop(i)
        ls.append(a)
        if ls[0]=="0":
            ls.pop(0)
            ls.append("0")
print(ls)


