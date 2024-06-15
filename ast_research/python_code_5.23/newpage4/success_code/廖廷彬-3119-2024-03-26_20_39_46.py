input_list = eval(input())
output_list = []
seen = set()

for elem in input_list[::-1]:
    if elem not in seen:
        output_list.insert(0, elem)
        seen.add(elem)
print(output_list)
