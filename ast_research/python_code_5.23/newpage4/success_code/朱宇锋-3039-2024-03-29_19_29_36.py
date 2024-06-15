nums=eval(input())
renums=nums.copy()
maxnums=max(nums)
minnums=min(nums)
for num in nums:
    if num ==maxnums or num == minnums:
        renums.remove(num)
print(renums)

