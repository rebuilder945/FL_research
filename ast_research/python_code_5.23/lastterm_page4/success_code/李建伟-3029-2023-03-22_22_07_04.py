names = list(input())
scores = eval(input())
lst = []
for i in range(len(names)):
    lst1 = [names[i],scores[i]]
    lst.append(lst1)
print(lst)
