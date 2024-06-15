x=eval(input())
y=[]
for i in x:
    for n in range(1,i):
        if i%n != 0:
            y.append(i)
            break
        else:
            continue
print(y)

