lst = eval(input())
a = 0
for i in range(len(lst)):
    a += lst[i]
b = a / len(lst)
if a % len(lst) == 0:
    print("%d"%b)
else:
    print("%.2f"%b)
