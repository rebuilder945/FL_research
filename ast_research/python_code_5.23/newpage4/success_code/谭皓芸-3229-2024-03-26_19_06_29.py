def find_unique_elements(nums):
    unique_elements = [num for num in nums if nums.count(num) == 1]
    return sorted(unique_elements) if unique_elements else False


input_list = eval(input())

result = find_unique_elements(input_list)
print(','.join(map(str, result)) if result else False)
