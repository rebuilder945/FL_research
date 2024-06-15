x=[]
for i in x:
    if i>=2:
        for a in range(2,i,1):
            if i%a==0:
                break
            else:
                x.append(i)
print(x)
