def calculate_average(nums):
    average = sum(nums) / len(nums)
    
    if average.is_integer():
        return int(average)
    else:
        return '{:.2f}'.format(average)

input_str = input()
input_list = eval(input_str)

result = calculate_average(input_list)
print(result)

