x=eval(input())
y=[]
for i in x:
    if i<=2:
       y.append(i)
    else:
        for j in range(2,i,1):
            if i%j!=0:
                y.append(i)
    print(y)
