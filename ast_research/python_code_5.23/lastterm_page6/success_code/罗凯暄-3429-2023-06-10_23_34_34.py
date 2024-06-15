s = input()
alpha_count = 0
space_count = 0
digit_count = 0
other_count = 0
for c in s:
    if c.isalpha():
        alpha_count += 1
    elif c.isspace():
        space_count += 1
    elif c.isdigit():
        digit_count += 1
    else:
        other_count += 1
print(alpha_count, space_count, digit_count, other_count)

