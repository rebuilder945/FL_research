lst=eval(input())
lst.sort(reverse=True)

n=int(len(lst))
sum=0
for i in range(n):
    a=lst[i]*(10**(n-i-1))
    sum+=a
print(a)

