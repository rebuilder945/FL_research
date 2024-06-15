names = input().split(",")
score = eval(input())
lst = []
for i in range(len(names)):
    lst.append([names[i],score[i]])
print(lst)
