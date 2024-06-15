a=eval(input())
c=[]
for x in range(len(a)):
    if x>1:
        for i in range(2,x):
            
            if (x%i)==0:
                break
        else:
            c.append(x)
print(c)
        

