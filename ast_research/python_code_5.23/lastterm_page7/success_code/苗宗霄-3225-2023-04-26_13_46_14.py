def work(a) :
    factorial_dict = {0:1} # 初始化字典，0的阶乘为1
    factorial = 1
    for i in range(1,a+1): # i从1到a循环
        factorial *= i # 计算i的阶乘
        factorial_dict[i] = factorial # 将i的阶乘存入字典
    return factorial_dict
	

a = int(input())
ans = work(a)
print(ans)

