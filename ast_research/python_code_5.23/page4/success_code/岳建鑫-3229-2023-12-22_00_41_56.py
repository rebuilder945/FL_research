def find_unique_elements(input_list):
    count_dict = {}
    for num in input_list:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    unique_elements = [key for key, value in count_dict.items() if value == 1]
    if len(unique_elements) == 0:
        return "False"
    else:
        return ','.join(map(str, sorted(unique_elements)))

input_str = input()

input_str = input_str.strip('[]')
input_list = list(map(int, input_str.split(',')))

output = find_unique_elements(input_list)
print(output)

