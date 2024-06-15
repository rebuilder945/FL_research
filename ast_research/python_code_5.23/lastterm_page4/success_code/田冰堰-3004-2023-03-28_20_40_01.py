ls=eval(input())
ls1=[]
ls2=[]
for i in ls:
    for j in range (2,i//2+1):
        if(i % j==0):
            break
        else:
            ls1.append(i)
ls2=list(set(ls1))
print((ls2))
