def find_longest_digit_substring(s):
    longest_substring = ""
    current_substring = ""
    has_digits = False

    for char in s:
        if char.isdigit():
            current_substring += char
            has_digits = True
        else:
            if has_digits:
                longest_substring = current_substring
            current_substring = ""
            has_digits = False

    if has_digits:
        longest_substring = current_substring

    if longest_substring:
        return longest_substring
    else:
        return "No digits"

