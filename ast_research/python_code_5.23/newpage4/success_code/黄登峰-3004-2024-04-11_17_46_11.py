a=input()
for i in a:
    if i==2 or 1:
        continue
    else:
        for x in range(2,int(i**0.5)):
            if i%x==0:
                a.remove(i)
                break
print(a)
            
