numbers = eval(input())
zeros_count = numbers.count(0)
non_zeros = [num for num in numbers if num != 0]
adjusted_list = non_zeros + [0] * zeros_count
print(adjusted_list)

