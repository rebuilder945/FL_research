lst=eval(input())
x=[]
for i in lst:
    if i>2:
        for y in range(2,i):
            if i%y==0:
                break
        else:
            x.append(i)
    elif i==2:
            y.append(i)
print(x)
