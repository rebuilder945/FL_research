n = int(input())
a = 2
b = 1
i = 0
s = 0
while n>0:
    c = a+b
    d = a
    a = c
    b = d
    s = s + a/b
    i = i+1
    if i == n:
        break
print("%.4f"(s))
