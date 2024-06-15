def remove_duplicates(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
        else:
            result.remove(i)
            result.append(i)
    return result
lst=input().split()
print(remove_duplicates(lst))
