
def remove_duplicates(input_str):
    lst = eval(input_str)
    a = lst[0]
    count = 0
    result = []
    for i in lst:
        if i == a:
            count += 1
            if count <= len(lst) - lst.index(a):
                result.append(i)
        else:
            result.append(i)
    return str(result)

input_str = eval(input())
output_str = remove_duplicates(input_str)
print(output_str)


