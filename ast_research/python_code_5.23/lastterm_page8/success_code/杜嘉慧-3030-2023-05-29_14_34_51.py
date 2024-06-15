def take(x):
    return x[1]
name = input().split(",")
score = input().split(",")
lst = []
pos = 0
for x in name:
    lst.append([x, int(score[pos])])
    pos += 1
lst.sort(key = take)
print(lst)

