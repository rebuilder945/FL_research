names = input().split(',')
scores = eval(input())
lst = []
a = len(names)
for i in range(a):
    lst.append([names[i],scores[i]])
print(lst)
