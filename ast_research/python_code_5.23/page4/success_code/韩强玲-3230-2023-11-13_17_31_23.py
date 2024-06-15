a = eval(input())
a.sort(reverse = True)
b = str(a[0])
for i in a[1:]:
    b +=str(i)
print(b)
