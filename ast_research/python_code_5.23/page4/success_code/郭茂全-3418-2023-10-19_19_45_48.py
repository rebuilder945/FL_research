def maxsum(nums):
    a=nums
    n=len(a)/2
    n=int(n)
    for b in range(n):
        y=max(nums)
        sum_max+=y
    return sum_max




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

