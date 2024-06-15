a=eval(input())
b=[]
for i in range(len(a)):
    c=a[i-1]
    if c == 2:
        b.append(c)
    else:
        for x in range(2,c):
            if c % x == 0:
                break
            else:
                b.append(c)
                break
print(b)
