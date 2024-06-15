a=eval(input())
b=[]
for i in a:
    if i <=1:
        continue
    else:
        for x in range(2,i//2+1):
            if i%x==0:
                break
        else:
            b.append(i)
print(b)


    





