ls=eval(input())
ls2=[]
for i in ls:
    if i>=2:
        for x in range(2,i):
            if i % x ==0:
                break
ls2.append(i)        
print(ls2)
        
