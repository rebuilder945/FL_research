nums = eval(input())
max  = max(nums)
min  = min(nums)
tmp = nums.copy()
for num in nums:
    if num == max  or num == min:
        tmp.remove(num)
print(tmp)
