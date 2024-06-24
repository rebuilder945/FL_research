lst=eval(input())
a=[]
for i in lst:
    for x in range(2,i):
        if i%x==0:
            break
    else:
        a.append(i)
print(a)
            

