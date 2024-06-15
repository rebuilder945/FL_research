s = input()
letter = 0
space = 0
num = 0
other = 0
for i in s:
    if i.isalpha():
        letter += 1
    elif i.isspace():
        space += 1
    elif i.isdigit():
        num += 1
    else:
        other += 1
print(letter,space,num,other)

