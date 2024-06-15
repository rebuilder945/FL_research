def calDegrees (x):
    x=eval(input())
    b=list()
    for i in range(len(x)):
		c=x.count(x[i])
		b.append(c)
    return (max(b))



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

