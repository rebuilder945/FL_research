name = input().split(",")
score = input()
lst = []
for x in name:
    for i in score:
        lst.append([x,i])
print(lst)
