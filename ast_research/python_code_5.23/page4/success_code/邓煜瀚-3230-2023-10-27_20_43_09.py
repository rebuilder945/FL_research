a=eval(input())
a.sort(reverse=True)
for i in range(len(a)):
    a[i]=str(a[i])
b="".join(a)
print(b)
