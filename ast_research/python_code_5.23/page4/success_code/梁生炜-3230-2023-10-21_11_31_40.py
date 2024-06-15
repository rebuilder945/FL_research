ls=eval(input())
ls.sort()
ls2=[]
for i in range(len(ls)):
    n=(10**i)*ls[i]
    ls2.append(n)
print(sum(ls2))
