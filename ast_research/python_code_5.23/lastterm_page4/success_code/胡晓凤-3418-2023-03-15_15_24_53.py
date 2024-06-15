import random
min_nums=0
def maxsum(nums):
    nums=[]
    global i
    random.shuffle(nums)
    for i in range(0,len(nums),2):
        print(nums[i],nums[i+1])
        global min_nums
        min_nums=min_nums+min(nums[i],nums[i+1])
        nums.append(min_nums)
        return max(nums)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

