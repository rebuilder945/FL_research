import string 
dict = {}
for alphabet in string.ascii_lowercase:
    dict[alphabet] = 0
string_list = eval(input())
for s in string_list:
    for c in s:
        if c.isalpha():
            dict[c] += 1
for alphabet in string.ascii_lowercase:
    if dict[alphabet]!= 0:
        print(alphabet + "," + str(dict[alphabet]))
