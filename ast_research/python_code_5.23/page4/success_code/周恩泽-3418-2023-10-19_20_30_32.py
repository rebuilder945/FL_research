def maxsum(nums):
    nums.sort(reverse=True)
    print(nums)
    n2=len(nums)
    print(n2)
    n3=[]
    for x in nums[1::2]:
        n3.append(x)
        n4=sum(n3)
    return n4




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

