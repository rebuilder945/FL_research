name = input().split(",")
score = eval(input())
s = []
for x in range(len(name)):
    s.append([name[x],score[x]])
print(s)
