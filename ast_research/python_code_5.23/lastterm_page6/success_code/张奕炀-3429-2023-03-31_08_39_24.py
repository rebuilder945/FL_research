s = input()
letters = 0
space = 0
digit = 0
others = 0
for i in s:
    if i.isalpha():
        letters = letters + 1
    if i.isspace():
        space = space + 1
    if i.isdigit():
        digit = digit + 1
others = len(s) - letters -space - digit
print(letters,end=" ")
print(space,end=" ")
print(digit,end=" ")
print(others,end=" ")
