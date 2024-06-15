n = eval(input())
for i in range(0, n + 1):
    i_str = str(i)  # 将整数转换为字符串
    if len(i_str) < 3:  # 检查字符串长度是否小于3
        #当数字小于 100 时，字符串 i 的长度会不足 3，导致访问索引超出范围
        print("none")
        continue
    a = int(i_str[0])
    b = int(i_str[1])
    c = int(i_str[2])
    if a**3 + b**3 + c**3 == i:
        print(i)
    else:
        print("none")