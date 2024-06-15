a=eval(input())
ls=[]
for x in a:
    if x>=2:
        for i in range(2,x):
                if x%i==0:
                        break
        else:
            ls.append(x)
print(ls)
            
    
    








    



