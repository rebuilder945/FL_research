n = int(input())
original_list = list(range(1, n+1))
first_element = original_list[0]
for i in range(n - 1):
    original_list[i] = original_list[i + 1]
original_list[n - 1] = first_element
print(original_list)

