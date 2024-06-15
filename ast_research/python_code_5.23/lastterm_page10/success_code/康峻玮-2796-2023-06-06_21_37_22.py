input_str = input()
digit_strs = []
digit_str = ''
for char in input_str:
    if char.isdigit():
        digit_str += char
    else:
        if digit_str != '':
            digit_strs.append(digit_str)
            digit_str = ''
if not digit_strs:
    print('No digits')
else:
    longest_digit_str = max(digit_strs, key=len)
    print(longest_digit_str)
