n=eval(input())
ls=[x for x in range(1,n+1,1)]
ls1=[]
for i in ls[0:n-1:1]:
    ls1.append(i)
ls2=[ls[n-1]]+ls1
print(ls2)



