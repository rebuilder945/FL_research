s = input()
letters = 0
digit = 0
space = 0
others = 0
for c in s:
    if c.isalpha():
        letter += 1
    elif c.isdigit():
        digit += 1
    elif c.isspace():
        space += 1
    else:
        others += 1
print(letters,digit,space,others)

