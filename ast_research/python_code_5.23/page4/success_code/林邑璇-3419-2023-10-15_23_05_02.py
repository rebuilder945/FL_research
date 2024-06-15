def calDegrees(nums):
    b=0
    for i in nums:
        c=nums.count(i)
        if c>b:
            b=c
        else:
          d=1
    return(b)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

