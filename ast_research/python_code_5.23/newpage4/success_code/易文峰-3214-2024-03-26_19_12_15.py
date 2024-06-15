def move_zeros_to_end(lst):
    non_zero_elements = [num for num in lst if num != 0]
    zero_count = len(lst) - len(non_zero_elements)
    result = non_zero_elements + [0] * zero_count
    print(result)
input_list = eval(input())
move_zeros_to_end(input_list)
