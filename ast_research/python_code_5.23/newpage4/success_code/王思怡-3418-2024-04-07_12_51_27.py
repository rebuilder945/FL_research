a =[]
def maxsum(nums):
    nums.sort(reverse=True)
    for i in nums[1: :2]:
        a.append(i)
    v = sum(a)
    return v




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

