y=eval(input())
a=[]
for i in y:
    if i>1:
        for x in range(2,i,1):
            if i%x==0:
                break
            else:
                a.append(i)
print(a)
