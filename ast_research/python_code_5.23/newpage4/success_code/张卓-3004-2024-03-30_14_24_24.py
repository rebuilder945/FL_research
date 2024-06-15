a=list(eval(input()))
b=[]
for i in a:
    for n in range(2,n):
        if i%n!=0:
            continue
        else:
            b.append(i)
print(b)


