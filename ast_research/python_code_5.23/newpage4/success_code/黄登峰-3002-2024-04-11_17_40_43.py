a=input()
for i in a:
    if i==2 or 1:
        continue
    else:
        for x in range(2,i):
            if i%x==0:
                a.remove(i)
                break
print(a)
            
