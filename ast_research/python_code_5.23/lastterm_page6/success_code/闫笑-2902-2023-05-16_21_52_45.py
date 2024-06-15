n_sele=eval(input())
def Fibo(n):
    num1 = 0
    if n == 1:
        num1=1
    elif n ==2:
        num1 = 2
    else:
        num1 = Fibo(n-1) + Fibo(n-2)
    return num1
num2 = 0
for x in range(1,n_sele+1):
    num2+=Fibo(x+1)/Fibo(x)
print("%.4f" % num2)
