ls=eval(input())
ls.sort()
s=0
for i in range(len(ls)):
    s+=ls[i]*10**i
print(s)

