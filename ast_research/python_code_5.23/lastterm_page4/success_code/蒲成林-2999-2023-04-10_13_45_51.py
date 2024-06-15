input_str = input()
n, m = map(int, input().split())
input_list = input_str.split()
if n >= 0 and n < len(input_list) and m >= 0 and m < len(input_list):
    input_list[n], input_list[m] = input_list[m], input_list[n]
print(input_list)

