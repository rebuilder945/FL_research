names = list(input().split(","))
scores = eval(input())
xin = []
for x in range(len(names)):
    xin.append(names[x],scores[x])
print(xin)
