h = eval(input())
N = eval(input())
sum = h
for i in range(1,N):
    sum = sum + 2*h/i
print("%.2f"%sum)
