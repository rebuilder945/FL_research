ls=eval(input())
for i in range(len(ls)-1,-1,-1):
    if ls[i]==0:
        a=ls.pop(i)
        ls.append(a)
    elif ls[0]=="0":
            ls.pop(0)
            ls.append("0")
print(ls)
