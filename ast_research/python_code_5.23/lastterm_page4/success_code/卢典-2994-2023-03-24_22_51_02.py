def repeat_element(lst, n, m):
    if abs(n) > len(lst):
        return "error"
    else:
        index = n if n >= 0 else len(lst) + n
        element = lst[index]
        lst += [element] * m
        return lst
lst=eval(input())
n,m=eval(input())
print(repeat_element(lst, n, m))
