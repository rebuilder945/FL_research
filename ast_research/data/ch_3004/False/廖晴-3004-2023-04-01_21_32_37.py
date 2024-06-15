s=eval(input())


for i in s:
    for x in range(2,i):
        
        if i%x==0:
            s.remove(i)
            break
print(s)


