def Fibonacci(num, n):
    while len(num) < n:
        num.append(num[-1] + num[-2])
    return num[n-1]

if __name__ == "__main__":
    num = [1, 1]
    n = int(input("请输入一个大于2的整数: "))
    result = Fibonacci(num, n)
    print(result)





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


