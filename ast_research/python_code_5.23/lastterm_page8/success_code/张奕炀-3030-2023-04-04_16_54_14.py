name = input().split(",")
answer = input().split(",")
answer = list(map(int,answer))
he = []
for i in range(len(name)):
    he.append([name[i],answer[i]])
print(he)
