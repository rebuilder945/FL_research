def maxsum(nums):
    nums1=0
    d=int(len(nums))
    nums2=sorted(nums)
    for x in range(0,d):
        if x%2=0:
        nums1+=nums2[x]
        
        
    return nums

    





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

