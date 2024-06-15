def maxsum(nums):
    nums.sort()
    a=0
    for i in range(len(nums)):
        if i%2==0:
            a+=nums[i]
        else :
            pass
        return(i)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

