def maxsum(nums):
    leng=len(nums)
    for i in range(leng):
        for j in range(leng-i-1):
            if nums[j]<nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    sum1=0
    ilen=int(leng/2)
    for k in range(ilen):
        sum1+=nums[k*2+1]
    return sum1




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

