s = input()
english = 0
space = 0
number = 0
other = 0
for i in s:
    if "0" <= i <= "9":
        number += 1
    elif "a" <= i <= "z":
        english += 1
    elif i == " ":
        space += 1
    else:
        other += 1
print(english,space,number,other)
