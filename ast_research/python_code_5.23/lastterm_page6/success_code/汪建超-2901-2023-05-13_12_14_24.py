sum = 0   # 记录数值总和
count = 0   # 记录数值个数
while True:
    s = input()   # 从键盘读入字符串
    if s == '#':   # 如果输入的是#，则退出循环
        break
    value = int(s)   # 将读入的字符串转换为整数
    sum += value   # 更新数值总和
    count += 1   # 更新数值个数
print(count, sum)   # 输出结果

