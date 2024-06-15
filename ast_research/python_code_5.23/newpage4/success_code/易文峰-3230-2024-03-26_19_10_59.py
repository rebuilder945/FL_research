def max_number_from_list(lst):
    lst.sort(reverse=True)
    result = ''.join(map(str, lst))
    return int(result)
input_list = eval(input())
result = max_number_from_list(input_list)
print(result)
