n=eval(input())
ls=[x for x in range(1,n+1,1)]
ls1=[]
for i in ls[1:n:1]:
    ls1.append(i)
ls2=ls1+[ls[0]]
print(ls2)



