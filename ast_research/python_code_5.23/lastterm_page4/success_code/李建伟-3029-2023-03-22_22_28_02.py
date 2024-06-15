names = list((input().split(",")))
scores = eval(input())
lst = []
for i in range(len(names)):
    lst1 = list(names[i],scores[i])
    lst.append(lst1)
print(lst)
