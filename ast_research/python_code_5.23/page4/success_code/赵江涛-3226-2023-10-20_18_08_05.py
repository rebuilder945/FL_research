def search(nums):
 for num in nums:
    if count == 0:
        candidate = num
    if num == candidate:
        count += 1
    else:
        count -= 1

 count = 0
 for num in nums:
    if num == candidate:
        count += 1

 if count > len(nums) // 2:
    return candidate
 else:
    return False






nums = eval(input())
y = search(nums)
print(y)


