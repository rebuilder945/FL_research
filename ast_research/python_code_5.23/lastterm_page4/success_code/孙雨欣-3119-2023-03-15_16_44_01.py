ls1=eval(input())
ls2=[]
for i in range(len(ls1)-1,-1,-1):
    if not ls1[i] in ls2:
        ls2.insert(0,ls1[i])
print(ls2)
