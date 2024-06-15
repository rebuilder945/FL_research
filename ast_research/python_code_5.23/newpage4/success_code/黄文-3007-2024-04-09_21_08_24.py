lst = eval(input())
n, m = map(int, input().split(','))
if n < 0 or m >= len(lst) or n > m:
    print("error")
else:
    result_list = lst[:n] + lst[m:]
    print(result_list)

       
