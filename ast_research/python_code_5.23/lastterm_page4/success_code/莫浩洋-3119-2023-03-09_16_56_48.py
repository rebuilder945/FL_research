a=list(eval(input()))
for i in a:
    b=a.count(i)
    if b==1:
        continue
    else :
        for x in range(0,b-1):
            a.remove(i)
print(a)
