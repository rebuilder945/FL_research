input_str = input()
input_list = input_str.split()
n, m = map(int, input().split())
if 0 <= n < len(input_list) and 0 <= m < len(input_list):
    input_list[n], input_list[m] = input_list[m], input_list[n]
print(input_list)
