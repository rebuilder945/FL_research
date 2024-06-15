def find_unique_elements(nums):
    unique_elements = []
    for num in nums:
        if nums.count(num) == 1:
            unique_elements.append(num)
    if not unique_elements:
        return False
    return sorted(unique_elements)
nums = list(map(int, input().split()))
result = find_unique_elements(nums)
print(result)



