ls=list(input())
n=str(input())
ls1=ls.copy()
for x in ls:
    if x==n:
        ls1.remove(x)
print("".join(ls1))
