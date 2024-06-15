#根据用户输入的月份，打印该月份所属的季节，如果输入的数据不在1~12范围内，输出“error" 
#提示：3，4，5 spring ；6，7，8 summer ；9，10，11 autumn ；12，1，2 winter
lst1=[3,4,5]
lst2=[6,7,8]
lst3=[9,10,11]
lst4=[12,1,2]
mon=eval(input())
if mon in lst1:
    print('spring')
elif mon in lst2:
    print('summer')
elif mon in lst3:
    print('autumn')
elif mon in lst4:
    print('winter')
else:
    print('error')
    
