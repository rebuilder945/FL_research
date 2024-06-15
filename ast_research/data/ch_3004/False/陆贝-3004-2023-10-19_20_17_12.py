lt=eval(input())
ls=[]
ii=[]
for x in lt:
    if x!=0 and x!=1 and x!=2 and x!=3:
        for i in range(3,x):#这里错写成了：
            if x%i==0:
                ls.append(x)
    elif x==0:
        ls.append(x)
    elif x==1:
        ls.append(x)
for y in lt:
    if y not in ls:
        ii.append(y)
print(ii)




    
    


