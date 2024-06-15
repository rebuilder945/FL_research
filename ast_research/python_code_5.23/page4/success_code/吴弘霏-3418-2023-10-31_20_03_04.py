def maxsum(nums):
    a=[]
    b=[]
    b=len(nums)
    for i in range(0,int(b/2)):
        if i not in a:
            nums.remove(max(nums))
            b.append(max(nums))
    return sum(b)





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

