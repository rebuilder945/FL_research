#读入一个整数列表，输出删除最大元素和最小元素后的列表。最大元素和最小元素可能有多个。
nums = eval(input())
result = []
for x in nums:
    if x == max(nums):
        continue
    elif x == min(nums):
        continue
    else:
        result.append(x)
print(result)

