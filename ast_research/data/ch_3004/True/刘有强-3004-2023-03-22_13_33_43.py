nature=eval(input())
sss=[]
for i in nature:
    if i == 2 or i == 3:
        sss.append(i)
    else:
        k=0
        for j in range(1,i+1):
            if i % j == 0:
                k += 1
        if k == 2:
            sss.append(i)
print(sss)
