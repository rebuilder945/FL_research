def find_unique_elements(nums):
    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    unique_elements = []
    for num in nums:
        if count_dict[num] == 1:
            unique_elements.append(num)
    
    if len(unique_elements) == 0:
        return False
    
    unique_elements.sort()
    return unique_elements


