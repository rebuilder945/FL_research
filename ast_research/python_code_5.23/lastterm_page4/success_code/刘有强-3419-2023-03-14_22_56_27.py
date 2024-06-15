def calDegrees(nums):
    max=0
    length=len(nums)
    for i in range(0,length-1):
        count=1
        for j in range(i,length):
            if(nums[i]==nums[j]):
               count+=1
               if(max<count):
                  max=count-1

    return max


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

