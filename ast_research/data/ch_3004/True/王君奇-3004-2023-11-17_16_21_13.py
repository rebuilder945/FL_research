x=eval(input())
y=[]
for i in x:
    if 1<i<2:
       y.append(i)

    elif i>=2:
        for j in range(2,i,1):
            if i%j==0:
                break
        else:
            y.append(i)    
print(y)
