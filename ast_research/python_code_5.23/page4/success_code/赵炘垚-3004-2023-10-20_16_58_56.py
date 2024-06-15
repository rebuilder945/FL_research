a=eval(input())
x=[]
for i in a:
    if i>=2:
        for j in range(2,x,1):
            if i%j==0:
                break
        else:
            x.append(i)
print(x)
