def maxsum(nums):
    a=[]
    b=len(nums)
    nums.sort()
    for i in nums(0,int(b),2):
        a.append(i)
    return sum(a)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

