def largest_number(single_digit_numbers):
    largest_str=".join(sorted(single_digit_numbers,reveres=True))"
    largest_number=int(largest_str)
    return largest_number
