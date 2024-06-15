x = 2
y = 1
sum1 = 0
n = eval(input())
for i in range(n):
    sum1 = sum1+x/y
    m = y
    y = x
    x = m+x
print("%.4f"%sum1)

    


