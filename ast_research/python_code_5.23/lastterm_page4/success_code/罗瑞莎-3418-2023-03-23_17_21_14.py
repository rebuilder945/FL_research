def maxsum(nums):
    lst = nums.sort(reverse=True)
    lst1 = list(map(int,lst))
    a = len(lst1)/2
    v = lst1[a-1]+lst1[-1]
    return v




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

