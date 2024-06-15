name = input()
grade = eval(input())
names = [x for x in name.split(',')]
n_list = [[0 for y in range(2)] for x in range(len(names))]
for z in range(len(names)):
    n_list[z-1][0] = (names[z-1])
    n_list[z-1][1] = (grade[z-1])
print(n_list)
