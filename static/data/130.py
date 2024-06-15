def f(x):
    if x < 20:
        return 6*x*x + 1
    elif 20 <= x < 40:
        return (3*x-60)**(1/2)
    else:
        return 100/(x+1)

x = int(input("Enter a number: "))  # 确保将输入转换为整数
result = f(x)
print(f"{result:.2f}")
#错误尝试对函数 f 本身使用格式化操作，而不是对函数的返回值进行格式化。