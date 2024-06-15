def work(a) :
factorial_dict = {0:1} # 初始化字典，0的阶乘为1
    factorial = 1 # 记录当前阶乘

    for i in range(1, x+1): # 从1~x遍历
        factorial *= i # 计算i的阶乘
        factorial_dict[i] = factorial # 将i的阶乘存入字典
    
    return factorial_dict # 返回字典
	

a = int(input())
ans = work(a)
print(ans)

