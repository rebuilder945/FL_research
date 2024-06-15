def calDegrees(nums):
    degrees=[]
    for x in nums:
        degrees.append(nums.count(x))
        return max(degrees)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

