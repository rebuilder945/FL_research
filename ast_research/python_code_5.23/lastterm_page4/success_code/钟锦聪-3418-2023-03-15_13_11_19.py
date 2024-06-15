def maxsum(nums):
    sum = 0
    nums.sort()
    for x in nums:
        a = int(nums.index(x))
        if a %2 ==0:
            sum += x
    return(sum)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

