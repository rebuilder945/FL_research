str_dict = {}
while True:
    s = input().strip()
    if s == 'q':
        break
    if s in str_dict:
        str_dict[s] += 1
    else:
        str_dict[s] = 1
max_str = max(str_dict, key=str_dict.get)
print(max_str, str_dict[max_str])

