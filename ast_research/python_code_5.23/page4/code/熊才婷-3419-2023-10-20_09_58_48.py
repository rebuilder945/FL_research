def calDgrees(x):
    list=[]
    for i in range(len(nums)):
        m=num[i]
        for z in range(len(nums)):
            n=nums[z]
            if m=n:
                x+=1
        list.append(x)
return max(list)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

