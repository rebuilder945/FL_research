def remove_duplicates(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst

print(remove_duplicates([元素1, 元素2, ..., 元素n]))

