t=eval(input())
for x in t:
    if 0.5<x<2:
        t.remove(1)
    elif x<0.5:
        t.remove(0)    
    else:
        for i in range(2,x):
            if  x%i==0:
                t.remove(x)
                break
print(t)    

     


