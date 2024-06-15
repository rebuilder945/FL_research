lst=eval(input())
b=[]
for x in lst:
    for a in range(2,x):
        if x%a==0:
            continue
        else:
            break
    b.append(x)
print(b)


