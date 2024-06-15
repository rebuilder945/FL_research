ls=eval(input())
n=len(ls)
ls1=ls.copy()
for i in range(n):
    if ls[i]==0:
        ls1.remove(0)
        ls1.append(0)
print(ls1)
