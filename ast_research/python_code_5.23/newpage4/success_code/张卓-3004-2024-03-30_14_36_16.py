a=list(eval(input()))
b=[]
for i in a:
    for n in range(2,i):
        if i%n!=0:
            m=1
            continue
    if m==1:
        b.append(i)
print(b)


