lst=eval(input())
ls2=[]

for x in lst:
    for y in range(2,x):
        if x%y==0 or x==0 or x==1:
            break
    else:
        ls2.append(x)
print(ls2)
        
                       
