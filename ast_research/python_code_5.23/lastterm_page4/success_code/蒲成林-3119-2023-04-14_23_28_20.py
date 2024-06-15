def remove_duplicates(lst):
    result = []
    for i in reversed(lst):
        if i not in result:
            result.insert(0, i)
    return result

lst = eval(input())
print(remove_duplicates(lst))
