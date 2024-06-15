def maxsum(nums):
    for i in nums:
        for j in nums:
                if nums.index(i) != nums.index(j):
                    c = j+i
                else :
                     continue
    return(c)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

