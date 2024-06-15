t=eval(input())
for x in t:
    for i in range(4,x):
        if x%i==0:
            t.remove(i)
            break
print(t)    

     
