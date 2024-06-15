def work(a) :
      dic = {0: 1}  # 初始化字典，保存0的阶乘
      fact = 1  # 初始化阶乘变量，用于计算1~a的阶乘
      for i in range(1, a+1):  # 计算1~a的阶乘
          fact *= i
          dic[i] = fact
      return dic
	

a = int(input())
ans = work(a)
print(ans)

