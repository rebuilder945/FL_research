lst=eval(input())
lst.sort()
n=int(len(lst))
for i in range(n):
    a=lst[i]*(10**(n-i))

print(a)

