a=eval(input())
a.sort(reverse=True)
n=len(a)
max=0
for x in a:
    max=max+x*10**(n-1)
    n=n-1
print(max)


