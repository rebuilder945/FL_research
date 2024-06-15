def find_most_frequent_string():
    string_list = input().split()
    string_dict = {}
    for string in string_list:
        if string in string_dict:
            string_dict[string] += 1
        else:
            string_dict[string] = 1
    max_count = max(string_dict.values())
    max_string_list = []
    for string, count in string_dict.items():
        if count == max_count:
            max_string_list.append(string)
    max_string_list.sort()
    for max_string in max_string_list:
        print(max_string, max_count)

find_most_frequent_string()


