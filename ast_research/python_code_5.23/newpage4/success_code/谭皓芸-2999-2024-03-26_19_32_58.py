input_str = input().split()
n, m = map(int, input().split())
input_str[n], input_str[m] = input_str[m], input_str[n]
print(input_str)
