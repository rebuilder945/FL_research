a=list(eval(input()))
upper=max(a)
lower=min(a)
list=[]
i=2
for i in a:
    if i==1:
        pass
    if i==2:
        list.append(i)
    if i!=2 and i!=1:
    
        for j in range(2,i):
            if i%j==0:
                break
        else:
             list.append(i)
print(list)
