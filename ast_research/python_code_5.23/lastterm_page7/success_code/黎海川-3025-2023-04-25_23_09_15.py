
str_list = input().split()

count_dict = {}
max_count = 0  
for s in str_list:
    count_dict[s] = count_dict.get(s, 0) + 1  
    if count_dict[s] > max_count:
        max_count = count_dict[s]  
for k, v in count_dict.items():
    if v == max_count:
        max_str_list.append(k)
max_str_list.sort()
for s in max_str_list:
    print(s, max_count)


