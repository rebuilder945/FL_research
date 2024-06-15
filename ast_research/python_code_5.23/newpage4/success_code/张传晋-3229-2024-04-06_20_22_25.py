def find_unique_elements(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    result = []
    for num in nums:
        if count[num] == 1:
            result.append(num)

    if len(result) == 0:
        return False

    result.sort()
    return result
nums = eval(input())
print(find_unique_elements(nums))

