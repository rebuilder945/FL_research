def Fibonacci(num,  n):
    num1 = 1
    num2 = 2
    sum = 2
    for x in range(0,n-2):
        temp2 = num2
        temp1 = num1
        temp = temp1 + temp2
        sum = sum + temp
        num2 = num1
        num1 = temp
    return sum




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


