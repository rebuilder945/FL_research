name = input().split(",")
score = input().split(",")
new = []
for i in range(len(name)):
    new.append([name[i],int(score[i])])
new.sort(key=lambda x:x[1])
print(new)
