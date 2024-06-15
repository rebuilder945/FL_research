def maxsum(nums):
    def maxsum(nums):
    n=len(nums)/2
    pairs=[nums[i:i+n] for i in range(0,len(nums),n)]
    b=sum([min(pairs) for pair in pairs])
    return(b)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

