#list
nums = eval(input())
ls = [num for num in nums if num!=0] + [num for num in nums if num == 0]
print(ls)
