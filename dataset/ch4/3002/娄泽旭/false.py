a = eval(input())
b=0
for i in range(len(a)):
    b = b+a[i]
    c = b/len(a)
if c%1 == 0:
    print(c)
elif c%1!=0:
    c = "%.2f"%c
    print(c)
