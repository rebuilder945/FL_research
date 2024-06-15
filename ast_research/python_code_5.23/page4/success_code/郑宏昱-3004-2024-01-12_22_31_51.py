n=eval(input())
m=[]
for i in n:
    if i>=2:
        for x in range(2,i):
            if i%x==0:
                break
        else:
                m.append(i)
print(m)
