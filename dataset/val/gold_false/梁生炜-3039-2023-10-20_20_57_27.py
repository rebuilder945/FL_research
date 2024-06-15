ls2=eval(input())
ls1=ls2.copy()
for i in ls2:
    if i>=max(ls1):
        ls2.remove(i)
print(ls2)
