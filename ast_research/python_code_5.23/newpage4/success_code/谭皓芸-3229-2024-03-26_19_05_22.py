def find_unique_elements(input_list):
    unique_elements = [num for num in input_list if input_list.count(num) == 1]
    if unique_elements:
        return ','.join(map(str, sorted(unique_elements)))[:-4]
    else:
        return False
input_list = list(input())
result = find_unique_elements(input_list)
print(result)
