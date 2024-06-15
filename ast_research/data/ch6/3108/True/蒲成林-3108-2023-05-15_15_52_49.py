#1
from collections import Counter

input_list = eval(input())
letter_count = Counter(''.join(input_list))

for letter in sorted(letter_count):
    print(f"{letter},{letter_count[letter]}")
