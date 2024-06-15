def remove_elements(lst, n, m):
    if n < 0 or m >= len(lst) or n > m:
        return "error"
    lst = lst[:n] + lst[m+1:]
    return lst

input_str = input()
lst = [int(x) for x in input_str.strip('[]').split(',')]
n, m = map(int, input().split(','))
result = remove_elements(lst, n, m)
print(result)

