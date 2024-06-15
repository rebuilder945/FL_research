def calDgrees(nums):
    index1=0
    max=0
    for i in range(len(nums)):
        flag=0
        for j in range(i+1,len(nums):
            if nums[j]==nums[i]:
                flag+=1
        if flag>max:
            max=flag
            index1=1
        return nums[index1]
        


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

