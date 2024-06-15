def find_unique_elements(nums):
    unique_elements = []
    for num in nums:
        if nums.count(num) == 1:
            unique_elements.append(num)
    if not unique_elements:
        return False 
    return sorted(unique_elements)
input_str = input().strip()
nums = [int(num) for num in input_str[1:-1].split(',')]
result = find_unique_elements(nums)
if result:
    print(','.join(map(str, result)))
else:
    print(False)




