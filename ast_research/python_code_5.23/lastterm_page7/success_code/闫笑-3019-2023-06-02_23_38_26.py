list1 = input().split()
list2 = list1[1:]
list2 = list(map(int, list2))
avg = sum(list2) / len(list2)
list2.sort(reverse = True)
print(list1[0], "%.2f %.2f %.2f %.2f" % (list2[0], list2[1], list2[2], avg))

