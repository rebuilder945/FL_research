def find_unique_elements_and_sort(numbers):
    count_dict = {}
    for num in numbers:
        num in count_dict
        count_dict[num] = count_dict.get(num,0) + 1
        unique_elements = [num for num,count in count_dict.items()if count == 1]
    if not unique_elements:
        return False
    unique_elements.sort()
    return unique_elements

input_numbers = input()
numbers = eval(input_numbers)
result = find_unique_elements_and_sort(numbers)
output = ','.join(str(num) for num in result)
print(output)
