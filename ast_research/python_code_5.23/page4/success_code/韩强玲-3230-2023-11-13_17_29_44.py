a = eval(input())
a.sort(reverse = True)
b = str(a[0])
for i in a:
    b +=str(i)
print(b)
