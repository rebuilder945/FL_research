string_list = input().split()
n, m = map(int, input().split())
string_list[n], string_list[m] = string_list[m], string_list[n]
print(' '.join(string_list))
