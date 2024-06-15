count = 0  # 计数器，记录输入整数的个数
total = 0  # 总和，记录输入整数的总和

while True:
    try:
        num = input()  # 从键盘输入一个数
        if num == '#':  # 如果输入#，则退出循环
            break
        num = int(num)  # 将输入的字符串转换为整数
        count += 1  # 计数器加1
        total += num  # 总和加上输入的整数
    except:  # 如果输入的不是整数，则忽略该输入
        pass

print(count, total)  # 输出计数器和总和


