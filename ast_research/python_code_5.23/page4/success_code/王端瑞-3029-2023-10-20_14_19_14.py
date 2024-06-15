names = input()

ls1 = names.split(',')

ls2 = eval(input())

matrix = [[ls1[i],ls2[i]] for i in range(len(ls1))]

print(matrix)
