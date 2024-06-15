st = input()
li = []
for i in st:
    li.append(i)
for j in li:
    if li.count(j) == 1:
        print(j)
        break
else:
    print("None")
