a = eval(input())
a.sort(reverse=True)
b = ""
for i in a:
    b += str(i)
print(int(b))

