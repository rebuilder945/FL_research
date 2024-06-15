def first_non_repeating_char(s):
    # create a dictionary to store the count of each character
    char_count = {}
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    # iterate through the string again to find the first non-repeating character
    for c in s:
        if char_count[c] == 1:
            return c
    # if no non-repeating character is found, return None
    return None
 # get input from user
s = input().strip()
 # call the function and print the result
result = first_non_repeating_char(s)
if result:
    print(result)
else:
    print("None")
