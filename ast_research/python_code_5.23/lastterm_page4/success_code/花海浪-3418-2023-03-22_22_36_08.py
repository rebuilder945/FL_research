def maxsum(nums):
    nums.sort()
    b=[]
    for x in range(1,4,2):
        b.append(x)
    return sum(b)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

