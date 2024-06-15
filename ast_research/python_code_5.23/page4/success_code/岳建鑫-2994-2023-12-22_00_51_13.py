def repeat_element(lst, n, m):
    if abs(n) >= len(lst):
        print("error")
        return
    if n < 0:
        n = len(lst) + n
    element = int(lst[n])
    lst.extend(int([element] * m))
    print(lst)

input_list = input().split(",")
n, m = map(int, input().split(","))
repeat_element(input_list, n, m)


