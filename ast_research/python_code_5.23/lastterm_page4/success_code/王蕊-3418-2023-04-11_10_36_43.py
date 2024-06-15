def maxsum(nums):
    b=[]
    z=0
    min_=0
    for i in range(int(len(nums)/2)):
        b.append(nums[z:(z+2)])
        z+=2
    for j in range(len(b)):
        min_+=min(b[j])




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

