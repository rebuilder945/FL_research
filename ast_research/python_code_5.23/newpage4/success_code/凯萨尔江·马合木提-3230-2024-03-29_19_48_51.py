def max_integer_from_digits(digits):
    sorted_digits=sorted(digits,reverse=True)
    max_integer=''.join(map(str,sorted_digits))
    return max_integer
digits_list=[0,1,2,3,2]
result=max_integer_from_digits(digits_list)
print(result)
