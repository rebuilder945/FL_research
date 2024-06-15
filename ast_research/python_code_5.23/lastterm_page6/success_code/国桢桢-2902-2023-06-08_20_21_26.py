def fbnq(num,n):
    a = num[0]
    b = num[1]
    fbnq = 1
    for i in range (n):
        if i <2:
            fbnq=1
        else:
            fbnq = a+b
            a = b
            b = fbnq
    return fbnq
num = [1,1]
n = eval(input())
x = 0
for i in range(2,n+2):
    x = x+fbnq(num,i+1)/fbnq(num,i)
print("%.4f"%x)
