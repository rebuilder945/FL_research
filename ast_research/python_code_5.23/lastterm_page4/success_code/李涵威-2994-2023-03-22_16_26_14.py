# 从一个列表中取出第n个元素，并重复m次，放到末尾，然后输出列表
# 输入一个整数列表和整数n(n可以是负数）和正整数m，从该列表中选择第n个元素，把该元素重复m次，然后放到列表的尾端，最后输出列表。
# 如果输入的n值不在列表下标范围之内，则输出"error"
nums_list = list(eval(input()))
(n,m) = eval(input())
if n >= len(nums_list):
    print("error")
else:
    temp = [nums_list[n]]*m
    nums_list.extend(temp)
    print(nums_list)
