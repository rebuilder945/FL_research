#1
# from collections import Counter

# input_list = eval(input())
# letter_count = Counter(''.join(input_list))

# for letter in sorted(letter_count):
#     print(f"{letter},{letter_count[letter]}")

#2
input_list = eval(input())
letter_count = {}

for string in input_list:
    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

for letter in sorted(letter_count):
    print(f"{letter},{letter_count[letter]}")
