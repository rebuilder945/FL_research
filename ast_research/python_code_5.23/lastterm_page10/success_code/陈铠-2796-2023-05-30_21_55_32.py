def find_longest_digits_substring(string):
    max_digits = ""
    current_digits = ""
    for char in string:
        if char.isdigit():
            current_digits += char
        elif current_digits:
            if len(current_digits) > len(max_digits):
                max_digits = current_digits
            current_digits = ""
    if max_digits:
        return max_digits
    else:
        return "No digits"
string = input()
result = find_longest_digits_substring(string)
print(result)
