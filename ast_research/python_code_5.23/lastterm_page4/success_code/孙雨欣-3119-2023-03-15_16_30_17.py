ls1=eval(input())
a=len(ls1)
ls2=[]
for i in range(a,-1,-1):
    if not ls1[i] in ls2:
        ls2.insert(0,ls1[i])
print(ls2)
