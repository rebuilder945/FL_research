lst = list(input())
a = input()
lst1 = []
for i in lst:
    if i != a:
        lst1.append(i)
print("".join(lst1))
