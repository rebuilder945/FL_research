count_dict = {}
while True:
    string = input()
    if string == "q":
        break
    count_dict[string] = count_dict.get(string, 0) + 1

max_count = 0
most_common_string = ""
for string, count in count_dict.items():
    if count > max_count:
        max_count = count
        most_common_string = string

print(most_common_string, max_count)
