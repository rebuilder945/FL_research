input_list=eval(input())
letter_count={}
for string in input_list:
    for char in string:
        if char.islower():
            if char in letter_count:
                letter_count[char]+=1
            else:
                letter_count[char]=1
for letter in sorted(letter_count.keys()):
    print(f"{letter},{letter_count[letter]}")
