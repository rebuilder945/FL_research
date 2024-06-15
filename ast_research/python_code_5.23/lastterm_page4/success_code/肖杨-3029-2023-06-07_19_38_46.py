a1 = list(input().split(","))
a2 = input()
a3 = [[]]*len(a2)
for i in range(len(a2)):
    a3[i].append(a1[i])
    a3[i].append(a2[i])
    print(a3)
