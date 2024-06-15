def remove_duplicates(lst):
    seen = set()
    i = len(lst) - 1
    while i >= 0:
        if lst[i] in seen:
            lst.pop(i)
        else:
            seen.add(lst[i])
        i -= 1
    return lst

input_str = "[4,3,2,3,2,4,True]"
input_list = eval(input_str)
output_list = remove_duplicates(input_list)
print(output_list)

