def maxsum(nums):
    nums.sort()
    list1=[]
    for i in range(0,len(nums),2):
        list1.append(nums[i])
return sum(list1)





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

