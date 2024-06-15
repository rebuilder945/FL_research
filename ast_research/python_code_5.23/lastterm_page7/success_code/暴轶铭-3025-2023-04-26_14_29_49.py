input_str = input("请输入一串字符串：")
str_list = input_str.split()

str_dict = {}
for str in str_list:
    if str in str_dict:
        str_dict[str] += 1
    else:
        str_dict[str] = 1

max_count = max(str_dict.values())
max_str_list = []
for k, v in str_dict.items():
    if v == max_count:
        max_str_list.append(k)

max_str_list.sort()
for max_str in max_str_list:
    print(max_str, max_count)
