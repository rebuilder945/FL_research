num_list = input().split(',')
num_list = [int(num) for num in num_list]
n, m = map(int, input().split(','))
if abs(n) < len(num_list):
    element = num_list[n]
    num_list.extend([element]*m)
    print(num_list)
else:
    print("error")
