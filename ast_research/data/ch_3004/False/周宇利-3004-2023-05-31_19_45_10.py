a=eval(input())
b=[]
for i in a:
    for x in range(2,i):
        if i%x:
            continue
        else:
            b.append(i)
print(b)
