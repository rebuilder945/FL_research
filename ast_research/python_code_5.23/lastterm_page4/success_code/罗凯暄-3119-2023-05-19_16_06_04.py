def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
        else:
            result.remove(item)
            result.append(item)
    return result
list = eval(input())
newlist = remove_duplicates(list)
print(newlist)
