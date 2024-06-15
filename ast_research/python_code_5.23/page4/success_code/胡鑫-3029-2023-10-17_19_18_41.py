names = list(input().split(","))
scores = eval(input())
re = []
for x in range (len(names)):
    re.append([names[x],scores[x]])
print(re)
