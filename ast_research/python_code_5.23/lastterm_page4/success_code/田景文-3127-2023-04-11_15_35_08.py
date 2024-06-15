sums = [x for x in range(1, int(input()) + 1)]
lst = []
for i in range(len(sums) - 1):
    lst.append(sums[i + 1])
lst.append(sums[0])
print(lst)

