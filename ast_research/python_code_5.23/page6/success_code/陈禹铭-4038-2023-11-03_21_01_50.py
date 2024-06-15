input_string=input()
letter_count=0
space_count=0
digit_count=0
other_count=0
for char in input_string:
    if char.isalpha():
        letter_count +=1
    elif char.isspace():
        space_count +=1
    elif char.isdigit():
        digit_count +=1
    else:
        other_count +=1
print(f"{letter_count}{space_count}{digit_count}{other_count}")
