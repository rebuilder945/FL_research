def move_zeros_to_end(lst):
    non_zero_elements = [x for x in lst if x != 0]
    zero_elements = [x for x in lst if x == 0]
    return non_zero_elements + zero_elements

input_str = input()
input_list = eval(input_str)
result = move_zeros_to_end(input_list)
print(result)

