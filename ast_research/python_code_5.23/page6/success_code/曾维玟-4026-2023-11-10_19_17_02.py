n = eval(input())
i = 0
a,b,c = 1,1,0
while i<n and i in range(1,n):
    c = c + (a+b)/(i + 1)
    a,b = a+b,n
    break
print("%.4f"%c)

