def find_unique(lst):
    count = {}
    for item in lst:
        count[item] = count.get(item, 0) + 1
    unique = [k for k, v in count.items() if v == 1]
    if unique:
        return eval(sorted(unique))
    else:
        return False
lst=eval(input())
print(find_unique(lst))
