h = eval(input())
n = eval(input())
sums = [h]
for i in range(1,n):
    H = h*0.5**i
    sums.append(H)
    sums.append(H)
print("%.2f"%sum(sums))


