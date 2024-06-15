def find_unique_elements(input_str):
    input_list = eval(input_str)
    element_count = {}
    for num in input_list:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1
    unique_elements = [num for num, count in element_count.items() if count == 1]
    if not unique_elements:
        return False
    unique_elements.sort()
    return ','.join(map(str, unique_elements))

input_str1 = "[1,2,3,5,2,3,4]"
input_str2 = "[9,9,9,12,12]"
print(find_unique_elements(input_str1))  # 输出：1,4,5
print(find_unique_elements(input_str2))  # 输出：False

