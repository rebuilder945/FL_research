def remove_duplicates(lst):
    new_lst = []
    last_occurrence = {}
    for i, item in enumerate(lst):
        if item not in last_occurrence:
            new_lst.append(item)
        else:
            if i - last_occurrence[item] > 1:
                new_lst.extend(lst[last_occurrence[item]+1:i])
            new_lst.append(item)
        last_occurrence[item] = i
    return new_lst
lst = eval(input())
newlst = remove_duplicates(lst)
print(newlst)

