a=int(input())
ls1=list(range(1,a+1))
b=0
n=0
for x in ls1:
    if b==0:
        n=x
        ls1[b]=ls1[b+1]
        b+=1
    
ls1[b]=n
print(ls1)
        

