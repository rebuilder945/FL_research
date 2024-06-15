lis=eval(input())
a=lis.copy()
for i in range(0,len(lis)):
    for j in range(2,(lis[i])):
        if ((lis[i])%j==0):
            a.remove(lis[i])
        break
a.remove(0)
a.remove(1)
print(a)

