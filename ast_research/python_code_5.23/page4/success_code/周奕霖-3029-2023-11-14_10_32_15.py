names =input().split(",")
scores = input()
b = list(zip(names,scores))
c = [[item[0], item[1]] for item in b]
print(c)
