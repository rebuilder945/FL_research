mon = eval(input())
if mon < 0 or mon >12:
    print('error')
elif mon in [3,4,5]:
    print('spring')
elif mon in [6,7,8]:
    print('summer')
elif mon in [9,10,11]:
    print('autumn')
else:
    print('winter')
