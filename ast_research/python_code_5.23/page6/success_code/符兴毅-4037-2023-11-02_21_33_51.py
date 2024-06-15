moon = eval(input())
if moon not in range(1, 13):
    print('error')
elif moon in [12, 1, 2]:
    print('winter')
elif moon in [3, 4, 5]:
    print('spring')
elif moon in [6, 7, 8]:
    print('summer')
elif moon in [9, 10, 11]:
    print('autumn')
else:
    print('error')

