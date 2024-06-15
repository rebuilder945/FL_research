def Fibonacci(num, n):
    if n <= len(num):
        return num[n-1]
    else:
        new_num = num[-1] + num[-2]
        num.append(new_num)
        return Fibonacci(num, n)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


