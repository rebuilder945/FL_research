input_list = input().strip().split(',')
input_list = [int(num) for num in input_list]
n, m = input().strip().split(',')
n = int(n)
m = int(m)
if abs(n) < len(input_list):
    selected_element = input_list[n]
    output_list = input_list + [selected_element] * m
    print(output_list)
else:
    print("error")


