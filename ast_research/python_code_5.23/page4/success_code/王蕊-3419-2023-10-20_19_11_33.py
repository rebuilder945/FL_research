def caldegrees(nums):
    Is2 = []
    for x in nums:
        wi = nums.count(x)
        Is2.append(wi)
    return max(Is2)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

