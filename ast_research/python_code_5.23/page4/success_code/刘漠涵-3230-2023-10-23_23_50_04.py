list0=eval(input())
list0=list(list0)
list0.sort(reverse=False)
b=0
for i in range(0,len(list0)):
    a=int(list0[i])*10**i
    b += a
print(b)
