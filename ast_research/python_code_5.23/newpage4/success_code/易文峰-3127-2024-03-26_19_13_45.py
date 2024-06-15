n = int(input())
num_list = list(range(1, n+1))
first_element = num_list[0]
for i in range(len(num_list)-1):
    num_list[i] = num_list[i+1]
num_list[-1] = first_element
print(num_list)
