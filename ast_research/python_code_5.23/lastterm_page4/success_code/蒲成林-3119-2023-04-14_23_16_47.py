# def remove_min_max(lst):
#     new_lst = [x for x in lst if x != max(lst) and x != min(lst)]
#     return new_lst

# lst=input()
# lst=eval(lst)
# print(remove_min_max([lst]))
def remove_min_max(lst):
    new_lst = [x for x in lst if x != max(lst) and x != min(lst)]
    return new_lst

lst = input()
lst = eval(lst)
print(remove_min_max(lst))
