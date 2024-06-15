def repeat_element(lst, n, m):
    if abs(n) >= len(lst):
        print("error")
        return
    if n < 0:
        n = len(lst) + n
    element = lst[n]
    lst.extend([element] * m)
    print(int.lst)

input_list = input().split(",")
n, m = map(int, input().split(","))
repeat_element(input_list, n, m)

