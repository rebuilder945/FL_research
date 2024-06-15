h = eval(input())
n = eval(input())
sum=0.0
sum += h
for i in range(n-1):
    h/=2
    sum += h*2
print(f"{sum:.2f}")
