lst=eval(input())
lst.sort()
for i in range(0,len(lst)):
    a=[lst[i]*(10**i)]
b=sum(a)
print(b)
