def find_majority_element(nums):
    if not nums:
        return False
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
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
result = find_majority_element(nums)
y=result






nums = eval(input())
y = search(nums)
print(y)


