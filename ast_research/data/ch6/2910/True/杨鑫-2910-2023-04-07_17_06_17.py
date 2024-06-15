h = eval(input())
N = eval(input())
sum = h
for i in range(N-1):
    h = h*0.5
    sum = sum +2*h
print("%.2f"%sum)
