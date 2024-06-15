lst=eval(input())
lst.sort(reverse=True)
n=len(lst)
total=0
m=n
for i in lst:
    m-=1
    total+=(i*10**m)
print(total)
print(lst)
