h = eval(input())
N = eval(input())
sum = h
for i in range(1,N):
    sum = sum + h/(2*i)*2
print("%.2f"%sum)
