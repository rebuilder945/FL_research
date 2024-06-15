lst=eval(input())
lst.sort(reverse=True)
total=0
n=len(lst)
for x in lst:
    total+=x*10**(n-1)
    n-=1
print(total)

