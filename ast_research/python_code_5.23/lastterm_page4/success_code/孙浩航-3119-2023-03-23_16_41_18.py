#9题库：删除列表中的重复值
def remove_duplicates(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)
        else:
            result.remove(x)
            result.append(x)
    return result

input_str = input()
lst = eval(input_str)
result = remove_duplicates(lst)
print(result)

