lis=eval(input())
a=lis.copy()
for i in range(0,len(lis)):
    for j in range(2,(lis[i])):
        if ((lis[i])%j==0):
            a.remove(lis[i])
        break
    if lis[i]%3==0:
        a.remove(lis[i])
        break
if 0 in a:
    a.remove(0)
if 1 in a:
    a.remove(1)
print(a)

