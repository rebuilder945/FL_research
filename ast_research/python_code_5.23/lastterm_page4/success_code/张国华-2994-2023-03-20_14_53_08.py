lst_str = input()
lst = eval("[" + lst_str + "]")
n, m = map(int, input().split(','))
if abs(n) > len(lst):
    print("error")
else:
    num = lst[n-1]
    lst += [num] * m
    lst = lst[:n-1] + lst[n-1+m:]
    lst.append(num)
    print(lst)
