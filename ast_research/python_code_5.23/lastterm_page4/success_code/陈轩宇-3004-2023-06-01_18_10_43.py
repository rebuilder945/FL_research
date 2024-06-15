a = eval(input())
for i in a:
    if i > 2:
        c = range(2,i)
        for x in c:
            if i%x==0:
                a.remove(i)
print(a)


                
    
