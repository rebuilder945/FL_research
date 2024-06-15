t=eval(input())
for x in t:
    if 1<x<4:
        continue
    else:
        for i in range(2,x):
            if x==1 or x%i==0 :
                t.remove(x)
                break
print(t)    

     


