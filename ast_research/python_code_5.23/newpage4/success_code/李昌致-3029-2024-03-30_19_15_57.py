names = eval(input())
grades = eval(input())
if len(names) == len(grades):
    a = [[names[i],grades[i]]for i in range(len(names))]
    print(a)
else:
    print('error')
