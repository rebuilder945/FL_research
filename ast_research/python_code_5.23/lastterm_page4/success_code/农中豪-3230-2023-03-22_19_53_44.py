a=eval(input())
a.sort(reverse=True)
b=''
for x in range(len(a)):
    b+=str(a[x])
print(b)
