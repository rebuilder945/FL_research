lst=eval(input())
lst.sort()
a=[lst[i]*(10**i) for i in range(0,len(lst))]
b=sum(a)
print(b)
