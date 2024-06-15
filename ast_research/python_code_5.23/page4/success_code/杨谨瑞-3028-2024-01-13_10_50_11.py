list1 = [int(x) for x in input().split(',')]
list=[list1[0]+i*list1[2] for i in range(list1[1])]
print(list)

