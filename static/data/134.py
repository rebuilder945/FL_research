n = eval(input())
c = []
if 100 < n < 1000:
    for x in range(100, n):
        temp_sum = 0
        temp_x = x
        for i in range(3):
            b = x % 10
            h = b**3
            x = x // 10
            temp_sum += h
        if temp_sum == temp_x:
            print(temp_sum)
    #循环结束条件的逻辑错误，
    #sum(c) 应该在每次循环内部进行重置。
else:
    print("none")
