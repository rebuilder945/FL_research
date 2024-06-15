n = eval(input())
sum = 0
for i in range(n):
    a,b = 2,1
    sum+=a/b
    a,b = (a+b),a
c = "%.4f"%sum
print(c)
