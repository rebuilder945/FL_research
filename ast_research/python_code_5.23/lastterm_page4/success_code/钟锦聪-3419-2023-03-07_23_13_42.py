def calDegrees(nums):
    iLili = []
    for x in nums:
        a = nums.count(x)
        iLili.append(a)
    return(max(iLili))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

