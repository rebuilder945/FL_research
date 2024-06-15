def find_unique_elements(input_list):
    count_dict = {}
    for num in input_list:
        count_dict[num] = count_dict.get(num, 0) + 1

    unique_elements = [num for num, count in count_dict.items() if count == 1]

    if not unique_elements:
        return False
    unique_elements.sort()

    return unique_elements

user_input = input()
input_list = eval(user_input)
result = find_unique_elements(input_list)
if result:
    print( ', '.join(map(str, result)))
else:
    print(False)


