x=1
y=2
sums = 0
n = eval(input())
while n >0:
    sums +=y/x
    x =y
    y = x + y
print("%.4f"%sums)
