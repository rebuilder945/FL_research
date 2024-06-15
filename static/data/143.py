x = eval(input())

if x < 20:
    y = 6 * x * x + 1
elif 20 <= x < 40:
    y = (3 * x - 60) ** (1 / 2)
else:
    y = 100 / (x + 1)

print("%.2f" % y)
#使用了"%.2f%"%y来进行格式化输出，但是在格式字符串中使用了两个百分号 %%，这导致了 "incomplete format" 错误。