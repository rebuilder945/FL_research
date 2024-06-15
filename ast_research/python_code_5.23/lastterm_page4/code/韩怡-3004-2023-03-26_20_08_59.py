l=list(input())
for i in l[:]:
    for j in range(2:int(i)):
        if j%i==0:
            l.remove(j)
print(l)
