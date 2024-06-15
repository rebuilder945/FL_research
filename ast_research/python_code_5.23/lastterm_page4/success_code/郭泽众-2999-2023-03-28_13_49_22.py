lst = input().split()
n , m = input().split()
lst[int(n)] ,lst[int(m)] = lst[int(m)] , lst[int(n)]
print(lst)
