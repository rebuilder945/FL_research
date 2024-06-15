def calDegrees(mostls):
    fuben={}
    for i in set(nums):
        fuben[i]=nums.count(i)
    return max(fuben)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

