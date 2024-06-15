ls=eval(input())
ls1=[]
for n in ls:
    if n>=2:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            ls1.append(n)         
print(ls1)        
