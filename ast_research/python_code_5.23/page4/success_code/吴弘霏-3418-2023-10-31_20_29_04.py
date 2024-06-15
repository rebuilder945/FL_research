def maxsum(nums):
    b=len(nums)
    c=[]
    for i in range(0,int(b/2)):
        nums.remove(max(nums))
        c.append(max(nums))
        nums.remove(max(nums))
    return sum(c)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

