def maxsum(nums):
    nums.sort()
    lst=[]
    for x in nums[::2]:
        lst.append(x)
        return(lst)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

