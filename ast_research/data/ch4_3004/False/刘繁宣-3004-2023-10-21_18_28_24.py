ls=eval(input())
ls2=[]
c=0
for i in ls:
    for j in range(2,i):
        if i % j == 0:
            c=c+1
            break
    if c==0:
        ls2.append(i)    
print(ls2)
        
