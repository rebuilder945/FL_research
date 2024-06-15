string = input()
if string == "":
    print("None")
else:
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    for char in string:
        if frequency[char] == 1:
            print(char)
            break



