import random
nums=[]
random.shuffle(nums)
min_nums=0
def maxsum(nums):
    for i in range(0,len(nums),2):
        print(nums[i],nums[i+1])
        min_nums=min_nums+min(nums[i],nums[i+1])
        nums.append(min_nums)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

