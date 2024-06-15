def calDgrees(nums):
    list=[]
    for i in range(len(nums)):
        m=num[i]
        x=0
        for z in range(len(nums)):
            n=nums[z]
            if m==n:
                x+=1
        list.append(x)
    a=max(list)
    return a


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

