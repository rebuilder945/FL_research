lst=input()[1:-1].split(",")
lst=[eval(i) for i in lst]
l2=[]
for x in lst:
    for i in range(2,x): 
        if x==1:
            l2.append(1)
        elif x%i==0:
            break
    else:
            l2.append(x)
print(l2)            


