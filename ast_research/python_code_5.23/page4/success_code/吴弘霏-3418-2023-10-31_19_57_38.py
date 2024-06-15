def maxsum(nums):
    a=[]
    for i in range(0,len(nums)/2):
        if i not in a:
            a.append(min(nums))
            nums.remove(min(nums))
    return sum(a)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

