n = int(input())
lst = [i for i in range(1, n+1)]
lst.append(lst[0])
lst = lst[1:]
print(lst)

