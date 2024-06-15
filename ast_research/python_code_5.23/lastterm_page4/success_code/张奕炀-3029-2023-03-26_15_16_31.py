name = input().split(',')
score = eval(input())
lst = []
for i in range(len(name)):
    lst.append([name[i],score[i]])
print(lst)
