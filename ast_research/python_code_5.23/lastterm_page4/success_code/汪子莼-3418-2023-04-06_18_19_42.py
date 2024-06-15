def maxsum(nums):
    nums.sort()
    a=[[nums[x].nums[x+1]]for x in range (0,len(nums)-1,2)]
    b=[]
    for i in a:
        c=min(i)
        b.append(c)
    return sum(b)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

