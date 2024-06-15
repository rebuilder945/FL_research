lst1 = list(eval(input()))
n, m = eval(input())
lst2 = lst1.copy()
if n <= len(lst1) and m <= len(lst2):
    for x in range (n,m):
        lst2.remove(lst1[x])
    print(lst2)
else:
    print("error")
