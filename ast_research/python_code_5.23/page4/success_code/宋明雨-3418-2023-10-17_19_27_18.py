def maxsum(nums):
    nums.sort()
    List1 = num[0:n+1]
    List2 = num[n+1: ]
    a,b=min(List1),min(List2)
    return a + b 




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

