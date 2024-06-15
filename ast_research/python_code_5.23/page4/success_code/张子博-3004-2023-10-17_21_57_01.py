t=eval(input())
for x in t:
    if x<4:
        continue
    else:
        for i in range(3,x):
            if x%i==0:
                t.remove(i)
                break
print(t)    

     


