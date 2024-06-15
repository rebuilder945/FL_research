ls1=input()
ls2=input()
ls1=list(ls1)
ls2=list(ls2)
ls11=ls1.copy()
for i in ls1:
    if i in ls2:
        ls11.remove(i)
print("".join(ls11))
