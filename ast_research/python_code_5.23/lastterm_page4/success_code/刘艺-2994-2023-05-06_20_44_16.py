list = list(eval(input()))
n,m = eval(input())
list2 = list.copy()
i = 1
a = list2[n]
if n <= len(list2):
    while i <= m:
        list.append(a)
        i += 1
    print(list)
else:
    print("error")

