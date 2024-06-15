a = list (set(eval((input())))) #set函数后面跟集合作为参数，要用eval,set过后类型变为set
a.sort(reverse = True)  #sort 函数参数不能为set
b = []
print(''.join(str(i) for i in a))
