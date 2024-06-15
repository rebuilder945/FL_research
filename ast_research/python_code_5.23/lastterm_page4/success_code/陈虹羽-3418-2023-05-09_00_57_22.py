def maxsum(nums):
    nums.sort()
    a=[]
    for i in range(0,len(nums),2):
        a.append(i)
    return sum(a)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

