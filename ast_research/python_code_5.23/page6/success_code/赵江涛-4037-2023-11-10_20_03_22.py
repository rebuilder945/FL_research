spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]
y = eval(input())
if y>=0 and y <=12:
    if y in spring:
        print('spring')
    elif y in summer:
        print('summer')
    elif y in autumn:
        print('autumn')
    else:print('winter')
else:print('error')
