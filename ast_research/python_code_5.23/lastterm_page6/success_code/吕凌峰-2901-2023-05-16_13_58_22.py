# 累积求和
# 【问题描述】从键盘不断地输入整数
# 当输入“#”时程序退出，然后打印出所输入整数的个数和总和
x = 0
Sum = 0
Count = -1
while x != "#":
    x = int(x)
    Sum += x
    Count += 1
    x = input()
print('%d %d' %(Count, Sum))
