a=eval(input())
b=[]
for i in a:
    if i==2:
        b.append(i)
    elif i>2:
        c=1
        for j in range(2,i):
            if i%j==0:
                c=0
                break
        if c==1:
            b.append(i)
print(b)
