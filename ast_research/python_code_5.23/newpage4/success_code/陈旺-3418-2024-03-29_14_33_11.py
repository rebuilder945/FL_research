def maxsum(nums):
    nums.sort(reverse=True)
    d=0
    for i in range(0,len,2):
        d+=i
    return(d)





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

