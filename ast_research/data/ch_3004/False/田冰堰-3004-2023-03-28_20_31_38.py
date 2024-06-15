ls=eval(input())
ls1=[]
ls2=[]
for s in ls:
    for i in range (2,s):
        if(s % i==0):
            break
        else:
            ls1.append(s)
ls2=list(set(ls1))
print((ls2))
