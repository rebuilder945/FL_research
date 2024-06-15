def remove_duplicates(lst):
    last_occurrence = {}
    result = []
    for i, item in enumerate(lst):
        if item in last_occurrence:
            del result[last_occurrence[item]]
        result.append(item)
        last_occurrence[item] = i
    return result
lst=input()
print(remove_duplicates(lst)) 
