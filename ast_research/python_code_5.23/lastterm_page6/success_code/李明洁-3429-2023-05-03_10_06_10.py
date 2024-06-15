s = str(input())
letter = 0
space = 0
digit = 0
other = 0
for i in s:
    if i.isletter():
        letter += 1
    elif i.isspace():
        space += 1
    elif i.isdigit():
        digit += 1
    else:
        other += 1
print(letter,space,digit,other)
