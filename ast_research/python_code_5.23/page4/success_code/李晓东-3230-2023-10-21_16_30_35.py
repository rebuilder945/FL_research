a = eval(input())
b = ""
a.sort(reverse=True)
for x in a:
    b = b+str(x)
b = int(b)
print(b)

