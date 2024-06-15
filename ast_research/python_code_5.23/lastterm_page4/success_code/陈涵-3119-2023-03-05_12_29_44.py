a=eval(input())
a2=a.copy()
for x in a2:
    cnt=a.count(x)
    if cnt>=2:
        for i in range(cnt-1):
            a.remove(x)
print(a)            

