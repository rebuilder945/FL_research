a = eval((not input())) #set函数后面跟集合作为参数，要用eval,set过后类型变为set
a.sort(reverse = True)  #sort 函数参数不能为set
if a[1] == 0:
    print(''.join(str(i) for i in a))
else:
    print('0')
