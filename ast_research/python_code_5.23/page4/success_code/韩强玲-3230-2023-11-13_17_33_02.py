a = eval(input())
a.sort(reverse = True)
b = str(a[0])
if sum(a)==0:
    print("0")
else:
    for i in a[1:]:
        b +=str(i)
print(b)
