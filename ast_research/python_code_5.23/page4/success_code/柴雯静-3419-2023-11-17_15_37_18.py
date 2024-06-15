def calDegrees(a):
       m = [a.count(x) for x in set(a)]
       return max(m)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

