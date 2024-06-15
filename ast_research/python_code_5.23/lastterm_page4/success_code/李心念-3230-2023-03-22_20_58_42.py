a = eval(input())
a.sort(reverse=True)
b = []
for i in range(len(a)):
    b1 = str(a[i])
    b.append(b1)
c =''
for i in range(len(a)):
    c = c+b[i]
if c !="000":
    print(c)
else:
    print("0")
