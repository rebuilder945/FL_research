ls1=eval(input())
n=0
ls2=[]
for x in ls1:
    for i in range(1,x+1):
        if x%i==0:
            n+=1
        else:
            continue
    if n==2:
        ls2.append(x)
    n=0
print(ls2)    
