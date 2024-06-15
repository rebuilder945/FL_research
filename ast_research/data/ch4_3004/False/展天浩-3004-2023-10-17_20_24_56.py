lst=input()[1:-1].split(",")
lst=[eval(i) for i in lst]
l2=[]
for x in lst:
    for i in range(2,x): 
        if x%i==0:
            break
        elif x==1:
            l2.append(x) 
    else:
            l2.append(x)
print(l2)            


