hws = []
hws1 = []
n = eval(input())
if type(n) == int:
    for num in range(2, n + 1):
        if str(num) == str(num)[::-1]:  # 检查是否是回文数
            hws.append(num)
            #这表明在调用 append() 方法时没有传递任何参数，
            #因此在使用 append() 方法之前，你需要先创建这个列表。

    for x in hws:
        for j in range(2, x):
            if x % j == 0:
                hws1.append(x)
                break
    for x in hws1:
        print(x, end=" ")
else:
    print("illegal input")