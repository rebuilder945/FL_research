
input_list = eval(input())
last_occurrence = {}
result = []
for item in input_list:
    last_occurrence[item] = input_list.index(item)
for index in sorted(last_occurrence.values()):
    result.append(input_list[index])
print(result)



