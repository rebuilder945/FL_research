# 月份对应的季节
n=eval(input())
if n not in range(1,13):
    print('error')
if n in [3,4,5]:
    print('spring')
elif n in [6,7,8]:
    print('summer')
elif n in [9,10,11]:
    print('autumn')
elif n in [1,2,12]:
# else:
    print('winter')
