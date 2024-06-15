def find_unique_elements(nums):
    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    unique_elements = [key for key, value in count_dict.items() if value == 1]
    
    if not unique_elements:
        return "False"
    else:
        return ','.join(map(str, sorted(unique_elements)))
n = eval(input())
print(find_unique_elements(n))
