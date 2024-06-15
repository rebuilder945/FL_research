a = eval(input())
b = 0
for i in range(len(a)):
    b = b+a[i]
c = b/len(a)
c = "%.2f"%c
print(c)
