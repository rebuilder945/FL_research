def sushu(n):
    for x in n:
        if x >= 2:
            for y in range(2,x):
                if x%y == 0:
                    break
                else:
                    list2.append(x)

list1 = eval(input())
list2 = []
sushu(list1)
print(list2)
