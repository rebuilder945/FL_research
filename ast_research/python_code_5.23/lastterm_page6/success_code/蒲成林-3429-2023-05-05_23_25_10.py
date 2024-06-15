string = input()

letters = 0
spaces = 0
digits = 0
others = 0

for char in string:
    if char.isalpha():
        letters += 1
    elif char.isspace():
        spaces += 1
    elif char.isdigit():
        digits += 1
    else:
        others += 1

print(letters, spaces, digits, others)
