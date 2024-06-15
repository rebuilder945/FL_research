lst=eval(input())
lst.sort(reverse=True)
print(lst)
n=int(len(lst))
sum=0
for i in lst:
    a=i*(10**(n-i))
    sum+=a
print(a)

