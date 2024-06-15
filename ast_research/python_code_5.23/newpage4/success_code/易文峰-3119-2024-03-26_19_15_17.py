def remove_duplicates(lst):
    seen = {}
    result = []
    
    for num in lst[::-1]:
        if num not in seen:
            result.insert(0, num)
            seen[num] = 1
    
    return result
input_list = eval(input())
result = remove_duplicates(input_list)
print(result)
