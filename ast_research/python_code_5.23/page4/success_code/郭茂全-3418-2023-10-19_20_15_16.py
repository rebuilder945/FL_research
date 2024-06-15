def maxsum(nums):
    n=len(nums)/2
    n=int(n)
    sum_max=0
    for b in range(n):
        x=max(nums)
        nums.remove(x)
        sum_max+=x
    return sum_max




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

