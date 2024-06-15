a=eval(input())
for i in a:
    if i==2:
        continue
    elif i>2:
        for x in range(2,i):
            if i%x==0:
                a.remove(i)
            else:
                continue        
print(a)
            
