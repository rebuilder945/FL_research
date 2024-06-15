def find_longest_digit_substring(s):
    longest_substring = ""
    current_substring = ""
    has_digits = False

    for char in s:
        if char.isdigit():
            current_substring += char
            has_digits = True
        else:
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            current_substring = ""

    # 检查最后的子串
    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring

    if has_digits:
        return longest_substring
    else:
        return "No digits"

