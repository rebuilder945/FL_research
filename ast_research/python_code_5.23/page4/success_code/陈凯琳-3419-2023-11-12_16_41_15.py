def calDegrees(nums):
    a=list(set(nums))
    lit=[]
    for i in a:
        lit.append(nums.count(i))
    return max(lit)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

