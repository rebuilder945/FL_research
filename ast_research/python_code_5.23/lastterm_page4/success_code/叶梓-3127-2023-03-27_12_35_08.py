n=eval(input())
ls1=range(1,n+1)
ls2=[]
for i in range(1,n):
    ls2.append(ls1[i])
ls2.append(ls1[0])
print(ls2)
