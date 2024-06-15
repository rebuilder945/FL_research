lt=eval(input())
ls=[]
for x in lt:
    if x!=0 and x!=1 and x!=2 and x!=3:
        for i in range(3,x):#这里错写成了：
            if x%i!=0:#这里错写成==
                ls.append(x)
    elif x==3:
        ls.append(3)
    elif x==2:
        ls.append(2)
print(ls)

    
    


