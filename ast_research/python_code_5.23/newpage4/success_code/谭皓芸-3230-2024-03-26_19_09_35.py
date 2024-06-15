def max_integer_from_list(lst):
    return int(''.join(map(str, sorted(lst, reverse=True))))
input_list = eval(input())
print(max_integer_from_list(input_list))
