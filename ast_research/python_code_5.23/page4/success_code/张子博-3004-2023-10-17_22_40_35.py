t=eval(input())
for x in t:
    if 1<x<4:
        continue
    elif x<1.1 and x>=0.9:
        t.remove(1)
    else:
        for i in range(2,x):
            if   x%i==0:
                t.remove(x)
                break
print(t)    

     


