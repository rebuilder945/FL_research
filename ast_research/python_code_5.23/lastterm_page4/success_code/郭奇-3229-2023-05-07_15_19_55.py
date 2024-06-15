def find_unique(lst):
    """
    找出列表中只出现一次的元素，并升序输出
    如果没有只出现一次的元素，则输出False
    """
    unique_lst = []
    for i in lst:
        if lst.count(i) == 1:
            unique_lst.append(i)
    if len(unique_lst) == 0:
        return False
    else:
        return sorted(unique_lst)

lst=eval(input())
print(find_unique(lst))


