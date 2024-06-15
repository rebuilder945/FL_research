lst=eval(input())
lst.sort()
n=int(len(lst))
sum=0
for i in lst:
    a=lst[i]*(10**(n-i))
    sum+=a
print(a)

