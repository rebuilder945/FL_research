i=list(input())
i.sort(reverse=True)
x=len(i)
for i in i[0:]:
    y=i*10**x
    x-=1
print(y)
