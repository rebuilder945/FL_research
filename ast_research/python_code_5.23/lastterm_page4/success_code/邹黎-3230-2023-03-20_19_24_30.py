lst=eval(input())
lst.sort(reverse=True)
n=len(lst)
total=0
for i in lst:
    total+=i*10**(n-(lst.index(i)+1))
print(total)
print(lst)
