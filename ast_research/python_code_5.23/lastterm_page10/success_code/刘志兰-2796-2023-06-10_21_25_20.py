input_str = input()
digits = ''.join(filter(lambda x: x.isdigit(), input_str)).split()
if not digits:
    print("No digits")
else:
    longest_digit = max(digits, key=len)
    longest_digit_index = digits.index(longest_digit)
    last_longest_digit = None
    for digit in digits[longest_digit_index+1:]:
        if len(digit) == len(longest_digit):
            last_longest_digit = digit
    if last_longest_digit:
        print(last_longest_digit)
    else:
        print(longest_digit)
