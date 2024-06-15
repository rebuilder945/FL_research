from collections import Counter
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    counter1 = Counter(s1)
    counter2 = Counter(s2)
    return counter1 == counter2

input_str1 = input()
input_str2 = input()
print(is_anagram(input_str1, input_str2))
