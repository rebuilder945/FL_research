a=eval(input())
b=[]
for x in a:
    if x >=2:
        for j in range(2,x,1):
            if x%j==0:
                break
        else:
            b.append(x)
print(b)
            

