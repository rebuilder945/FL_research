nums=eval(input())
nums.sort(reverse=True)
nums_str="".join(str(x) for x in nums)
print(int(nums_str))
