name = input().split(",")
score = input().split(",")
new = []
for i in range(len(name)):
    new.append([name[i],int(score[i])])
print(new)
