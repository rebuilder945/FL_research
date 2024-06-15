a=list(eval(input()))
b=[]
for i in a:
    for n in range(2,n):
        if i%n!=0:
            continue
        else:
            m=1
    if m==1:
        b.append(i)
print(b)


