a=eval(input())
b=a.copy()
for i in a:
    if i==0:
        b.remove(i)
    elif i==1:
        b.remove(i)
    else:
        for x in range(2,i-1):
            if i%x==0:
                b.remove(i)
                break
                
print(b)
            

