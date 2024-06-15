names =list(input())
scores = input()
for i in range(len(names)):
    b = list(names[i]+scores[i])
    c = b.append(b)
print(c)

