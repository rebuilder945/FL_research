ls=eval(input())
a = len(ls)
for i in range(a):
    if ls[i]!=0:
        i+=1
    elif ls[i]==0:
        del ls[i]
        ls.append(0)
print(ls)
