n = int(input())  # 输入一个整数n
flag = False  # 标记是否有水仙花数
if n <= 1000:
    for i in range(100, n+1):  # 遍历每个三位数
        a = i // 100  # 百位数
        b = (i // 10) % 10  # 十位数
        c = i % 10  # 个位数
        if a**3 + b**3 + c**3 == i:  # 判断是否为水仙花数
            print(i)
        flag = True
elif n > 1000:
        for i in range(100, 1000):  # 遍历每个三位数
            a = i // 100  # 百位数
            b = (i // 10) % 10  # 十位数
            c = i % 10  # 个位数
            if a**3 + b**3 + c**3 == i:  # 判断是否为水仙花数
                print(i)
        flag = True
    

if not flag:  # 如果没有水仙花数
    print("none")

