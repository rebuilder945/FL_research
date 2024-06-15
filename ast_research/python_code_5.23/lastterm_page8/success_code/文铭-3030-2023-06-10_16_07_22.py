l1 = input().split(",")
l2 = int(input()).split(",")
lst = []
for x in range(len(l1)):
    lst.append([l1[x],l2[x]])
lst.sort(key =lambda x:x[1])
print(lst)
