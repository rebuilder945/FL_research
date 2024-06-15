s = input()

digits = ""
max_digits = ""
found_digits = False

for char in s:
    if char.isdigit():
        digits += char
        found_digits = True
    elif found_digits:
        max_digits = digits
        digits = ""
        found_digits = False

if found_digits:
    max_digits = digits

if max_digits:
    print(max_digits)
else:
    print("No digits")

