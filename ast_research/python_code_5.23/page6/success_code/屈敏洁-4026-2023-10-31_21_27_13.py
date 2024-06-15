n = int(input())
sum = 2
a = 2
b = 1
for x in range(n-1):
    a = a+b
    b = a-b
    c = a/b
    sum = sum + c
print("%.4f"%(sum))
