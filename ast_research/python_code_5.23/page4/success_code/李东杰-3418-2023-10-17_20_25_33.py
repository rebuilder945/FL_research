def maxsum(nums):
    a=0
    d=int(len(nums))
    nums2=sorted(nums)
    for x in range(0,d):
        if x%2==0:
            a+=nums2[x]
        
        
    return a

    





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

