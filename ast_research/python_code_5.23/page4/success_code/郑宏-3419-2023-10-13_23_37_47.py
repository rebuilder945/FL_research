def calDegrees(x):
		d=list()
		for i in range(len(x)):
			c=x.count(x[i])
			d.append(c)
		return (max(d))



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

