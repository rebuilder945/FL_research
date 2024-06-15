print(v)
def maxsum(nums):
    a=nums.sort()
    b=a[1::2]
    v=sum(b)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

