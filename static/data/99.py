h=eval(input())
N=eval(input())
s = str(h)
for i in range(N - 1):
    s += str(h * (0.5) ** i)
    #使用str() 函数将整数 h * (0.5) ** i 转换为字符串，以避免拼接整数和字符串的错误
print('%.2f' % float(s))
