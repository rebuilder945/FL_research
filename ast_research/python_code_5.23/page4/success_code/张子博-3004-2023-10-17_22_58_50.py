t=eval(input())
for x in t:
    if x<2:
        t.remove(1)
    else:
        for i in range(2,x):
            if   x%i==0:
                t.remove(x)
print(t)    

     


