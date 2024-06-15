
def calDegrees(m):
    n=[m.count(x) for x in set(m)]
    return max(n)
nums  =  eval(input())
d=calDegrees(nums)  #调用自定义函数
print(d)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

