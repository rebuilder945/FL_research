str_list = eval(input())
char_list = list(''.join(str_list))
char_set = set(char_list)
char_counter = []
list(map(lambda char: char_counter.append((char,char_list.count(char))), char_set))
char_counter.sort(key=lambda item: item[0])
for (char, count) in char_counter:
    print(f"{char},{count}")
