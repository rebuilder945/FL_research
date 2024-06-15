def largest_number_from_list(numbers):
    
    sorted_numbers = sorted(map(str, numbers), key=lambda x: x * 10, reverse=True)
    largest_number = int(''.join(sorted_numbers))
    return largest_number

user_input = input("")
numbers = eval(user_input)

result = largest_number_from_list(numbers)
print( result)

