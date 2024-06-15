list = list(eval(input()))
n,m = eval(input())
list2 = list.copy()
i = 1
if n <= len(list2):
    a = list2[n]
    while i <= m:
        list.append(a)
        i += 1
    print(list)
else:
    print("error")

