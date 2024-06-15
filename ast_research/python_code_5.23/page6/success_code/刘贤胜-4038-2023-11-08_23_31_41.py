s = input()
char_count, space_couny, num_count, other_count = 0, 0, 0, 0
for i in s:
    if "a"<=i<="z"or "A"<=i<="Z":
        char_count += 1
    elif i ==" ":
        space_couny += 1
    elif "g"<=i<="9":
        num_count += 1
    else:
        other_count += 1
print(char_count, space_couny, num_count, other_count)
