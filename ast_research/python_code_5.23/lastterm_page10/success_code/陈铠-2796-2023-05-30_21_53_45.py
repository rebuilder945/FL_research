def find_longest_digits_substring(string):
    longest_digits = ""
    current_digits = ""
    for char in string:
        if char.isdigit():
            current_digits += char
        else:
            if len(current_digits) > len(longest_digits):
                longest_digits = current_digits
            current_digits = ""
    if longest_digits:
        return longest_digits
    else:
        return "No digits"
string = input()
print(find_longest_digits_substring(string))
