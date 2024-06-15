l1 = input().split(",")
l2 = eval(input())
l3 = list(l1)
l4 = []
l5 = []
for i in range(len(l3)):
    l4 = (l3[i],l2[i])
    l5.append(l4)
print(l5)
