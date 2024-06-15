name = input().split(',')
goal = eval(input())
Ls = []
for v in range(len(name)):
    Ls.append([name[v],goal[v]])
print(Ls)
