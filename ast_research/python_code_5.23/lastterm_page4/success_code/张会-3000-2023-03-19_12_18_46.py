lst = eval(input())
a = 0
for i in range(len(lst)):
    a += lst[i]
b = a / len(lst)
print("%.2f"%b)
