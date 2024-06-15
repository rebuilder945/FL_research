def calDegrees(nums):
    nums = [1,2,3,3,4,5,4,3,3]
    n = 1
    for i in nums:
        if i not in nums:
            n(i) = 1
        else:
            n(i) += 1
        return max(n)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

