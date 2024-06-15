a=eval(input())
a.sort(reverse=True)
b=len(a)
c=""
for i in range(b):
    x=str(a[i])
    c=c+x
print(int(c))
