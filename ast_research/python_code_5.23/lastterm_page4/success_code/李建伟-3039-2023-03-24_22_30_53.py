def delete(nums):
    mx = max(nums)
    mn = min(nums)
    while mx in nums:
        nums.remove(mx)
    while mn in nums:
        nums.remove(mn)
    return nums
lst = eval(input())
lst1 = delete(lst)
print(lst1)

