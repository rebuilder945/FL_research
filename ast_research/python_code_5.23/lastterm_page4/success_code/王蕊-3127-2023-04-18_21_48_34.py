n=int(input())
ls1=list(range(1,n+1))
a=0
b=0
for x in ls1:
    if a==0:
        n=b
        ls1[a]=ls1[a+1]
        a+=1
ls1[a]=n
print(ls1)
        

