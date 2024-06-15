def calDegrees(nums):
    lst=[]
    for i in nums:
        m=nums.count(i)
    lst.append(m)
    return max(lst)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

