input_str = input()
str_list = input_str.split()
n, m = map(int, input().split())
str_list[n], str_list[m] = str_list[m], str_list[n]
print(str_list)

