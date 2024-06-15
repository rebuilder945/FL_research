n, m = map(int, input().split())
for i in range(n, m):
    for a in range(n, m):
        for c in range(n, m):
            shu = str(i) + str(a) + str(c)
            #在使用 str() 函数时，可能会遇到一个问题，即在一些情况下，整数前面可能会有一个零，这会导致错误
            shu1 = int(shu)  # 将字符串转换为整数
            if m - n != 3 or shu[0] == '0':  # 修改判断条件，将数字 0 转换为字符串 '0'
                print("illegal input")
            elif i != a and i != c and c != a:
                print(shu1, end=" ")
