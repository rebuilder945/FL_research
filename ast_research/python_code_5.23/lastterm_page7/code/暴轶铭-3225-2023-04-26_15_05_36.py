def work(a) :
ans = {0: 1}  # 初始值0! = 1
    factorial = 1
    for num in range(1, a+1):
        factorial *= num  # 累乘计算阶乘
        ans[num] = factorial  # 存入字典
    return ans
	

a = int(input())
ans = work(a)
print(ans)

