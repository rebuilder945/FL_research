input_list = input().split()
n, m = map(int, input().split())
input_list[n], input_list[m] = input_list[m], input_list[n]
print(input_list)
