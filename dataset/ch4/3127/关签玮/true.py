a=eval(input())
b=1
ls1=[b+1 for b in range(a)]
ls2=ls1.copy()
for i in range(len(ls1)-1):
    ls2[i],ls2[i+1]=ls2[i+1],ls2[i]
print(ls2)
