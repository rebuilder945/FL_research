def maxsum(nums):
    nums1=[]
    nums2=[]
    d=len(nums)/2
    for x in range(0,d):
        a=random.randint(0,2n) 
        c=nums.pop(a)
        nums1.append(c)
b=min(nums)
c=min(nums1)
e=b+c
nums2.appen(e)
    return max(nums2)

    





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

