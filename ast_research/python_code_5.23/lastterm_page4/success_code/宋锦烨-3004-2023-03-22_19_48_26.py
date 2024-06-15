a=eval(input())
b=[]
for i in range(len(a)):
    c=a[i]
    if c == 2:
        b.append(c)
    else:
        for x in range(2,c):
            if c % x == 0:
                break
        else:
            b.append(c)
b.remove(1)
print(b)
