names =list(input().split(","))
scores = input().split(",")
c = []
for i in range(len(names)):
    b = names[i],scores[i]
    c.append(b)
print(c)

