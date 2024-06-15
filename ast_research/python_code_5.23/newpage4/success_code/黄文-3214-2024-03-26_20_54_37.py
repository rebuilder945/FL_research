def move_zeros_to_end(input_list):
    non_zeros = [num for num in input_list if num != 0]
    zeros = [num for num in input_list if num == 0]
    adjusted_list = non_zeros + zeros

    print(adjusted_list)

user_input = input()
input_list = eval(user_input)

move_zeros_to_end(input_list)

