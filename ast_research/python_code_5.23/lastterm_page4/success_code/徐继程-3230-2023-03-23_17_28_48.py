lst=eval(input())
lst.sort()
n=int(len(lst))
sum=0
for i in range(n):
    a=lst[i]*(10**(n-i))
    sum+=a
print(a)

