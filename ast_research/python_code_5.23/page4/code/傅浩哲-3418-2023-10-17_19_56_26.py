def maxsum(nums):
    n=0
    nums.sort(reverse=ture)
    for i in range(len(nums)):
        if i%2=1:
            n+=nums(i)
return(n)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

