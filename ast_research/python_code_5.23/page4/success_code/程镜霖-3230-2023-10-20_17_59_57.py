lst=eval(input())
lst.sort()
x=0
for i in range(len(lst)):
    x+=lst[i]*10**i
print(x)


