a=eval(input())
for i in a:
    if i>=2:
        for m in range(2,i,1):
            if i%m==0:
                break
            else:
                a.append(i)
print(a)

