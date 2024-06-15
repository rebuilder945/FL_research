#输入一个整数列表和整数n(n可以是负数）和正整数m，从该列表中选择第n个元素，把该元素重复m次，然后放到列表的尾端，最后输出列表。
# 如果输入的n值不在列表下标范围之内，则输出"error"
nums = input().split(",")
n,m = eval(input())
if abs(n) < len(nums):
    nums.append(nums[n])
    nums.append(nums[n])
    nums.append(nums[n])
    result = [int(x) for x in nums]
    print(result)
else:
    print("error")




