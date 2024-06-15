ls1=eval(input())
m=[]
for i in ls1:
    if i>=2:
        for x in range(2,i,1):
            if i%x==0:
                break
        m.append(i)
print(m)

