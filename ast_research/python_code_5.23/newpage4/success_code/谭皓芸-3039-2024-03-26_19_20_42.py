def remove_max_min_elements(lst):
    if len(lst) < 2:
        return []
    
    max_val = max(lst)
    min_val = min(lst)
    
    result = [num for num in lst if num != max_val and num != min_val]
    return result
input_list = eval(input())
result = remove_max_min_elements(input_list)
print(result)
