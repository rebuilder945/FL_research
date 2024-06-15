def maxsum(nums):
    nums.sort(reverse=Ture)
    b=[]
    for i in range(len(nums)):
        if i%2==1:
            b.append(nums[i])
    rethrn sum(b)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

