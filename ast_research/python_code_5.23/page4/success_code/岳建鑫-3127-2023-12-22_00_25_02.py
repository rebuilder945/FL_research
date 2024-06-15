n = int(input())
my_list = list(range(1, n+1))

first_element = my_list[0]
for i in range(n-1):
    my_list[i] = my_list[i+1]
my_list[n-1] = first_element

print(my_list)

