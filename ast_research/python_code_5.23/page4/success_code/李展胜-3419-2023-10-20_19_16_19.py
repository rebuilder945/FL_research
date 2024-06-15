def calDegrees(a):
       n = [a.count(x) for x in set(a)]
       return max (n)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

