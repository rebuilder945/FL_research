names = input()
grades = eval(input())
names = names.split(',')
a = [[names[i],grades[i]]for i in range(len(grades))]
print(a)

