n=eval(input())
m=[]
for i in n:
    if i==2:
        m.append(i)
    else:
        for b in range(2,i):
            if i%b==0:
                m.append(i)
print(m)
