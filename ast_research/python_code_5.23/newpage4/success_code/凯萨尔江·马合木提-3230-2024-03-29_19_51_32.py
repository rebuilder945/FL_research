def max_integer_from_digits(digits):
    sorted_digits=sorted(digits,reverse=True)
    max_integer=''.join(map(str,sorted_digits))
    return max_integer

print(max_integer_from_digits())
