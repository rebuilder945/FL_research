def calDegrees(nums):
    max=0
    L=len(nums)
    for i in range(0,L):
        count=1
        for j in range(i+1,L):
            if(nums[i]==nums[j])
                count+=1
                if(max<count):
                    max=count
    return max


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

