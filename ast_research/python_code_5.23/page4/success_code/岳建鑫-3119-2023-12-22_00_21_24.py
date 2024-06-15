def remove_duplicates(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
        else:
            idx = len(new_lst) - new_lst[::-1].index(i) - 1
            new_lst = new_lst[:idx] + [i]
    return new_lst
input_str = input()
lst = eval(input_str)
result = remove_duplicates(lst)
print(result)

