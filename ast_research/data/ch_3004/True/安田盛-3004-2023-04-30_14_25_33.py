n=eval(input())
a=[]
for i in n:
    if i==2:
        a.append(i)
    elif i>2:
        for x in range(2,i//2+1):
            if i%x==0:
                break
        else:
            a.append(i)
print(a)



