lst=eval(input())
r=[]
for i in lst:
    if i ==2:
        r.append(i)
    else:
        for x in range(2,i):
            if i % x != 0:
                r.append(i)
                break
print(r)
