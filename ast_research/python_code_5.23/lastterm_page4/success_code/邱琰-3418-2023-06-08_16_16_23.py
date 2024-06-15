def maxsum(nums):
    ls=[]
    for i in range(len(nums)):
        if i%2==0:
            ls.append(nums[i])
        return sum(ls)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

