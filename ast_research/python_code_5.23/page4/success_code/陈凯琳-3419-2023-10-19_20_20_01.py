def calDegrees(nums):
    lit=list(set(nums))
    a=[]
    for i in range(len(lit)):
        a.append(nums.count(lit[i]))
    return max(a)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

