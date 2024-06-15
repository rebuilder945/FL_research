input_list = eval(input().strip())
last_occurrence = {}
for i, num in enumerate(input_list):
    last_occurrence[num] = i
output_list = [input_list[i] for i in sorted(last_occurrence.values())]
print(output_list)


