names = list((input().split(",")))
scores = eval(input())
lst = []
n = 0
for i in names:
    m = scores[n]
    lst1 = []
    lst1.append(i)
    lst1.append(m)
    lst.append(lst1)
    n = n + 1
print(lst)
