def remove_duplicates(lst):
    last_occurrence = {}
    result = []
    for i in range(len(lst)-1, -1, -1):
        if lst[i] not in last_occurrence:
            last_occurrence[lst[i]] = i
            result.insert(0, lst[i])
    return result


input_list = eval(input())
output_list = remove_duplicates(input_list)
print(output_list)

