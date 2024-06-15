def max_integer_from_one_digit_list(digits):
    sorted_digits=sorted(digits,reverse=True)
    max_integer=''.join(map(str,sorted_digits))
    return max_integer
input_list=[]
output=max_integer_from_one_digit_list(input_list)
print(output)
