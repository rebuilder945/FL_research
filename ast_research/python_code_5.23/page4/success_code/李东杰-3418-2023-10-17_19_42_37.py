def maxsum(nums):
    nums1=[]
    d=int(len(nums)/2)
    numssorted=sorted(nums)
    
    c=numssorted.pop(-2)
   
    b=min(nums)
    
    v=b+c
    return v

    





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

