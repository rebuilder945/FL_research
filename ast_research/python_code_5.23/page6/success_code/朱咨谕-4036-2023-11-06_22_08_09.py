#  从1号袋到10号袋，奇数的口袋是红色，偶数的口袋是黑色。
#  从11号袋到18号袋，奇数的口袋是黑色，偶数的口袋是红色。
#  从19号袋到28号袋，奇数的口袋是红色，偶数的口袋是黑色。 
# 从29号袋到36号袋，奇数的口袋是黑色，偶数的口袋是红色。
#  0号口袋是绿色
a=eval(input())
if a==0 : print('green')
elif a>0 and a<11 : 
    if a%2==0 : print('black')
    else : print('red')
elif a>10 and a<19 : 
    if a%2==0 : print('red')
    else : print('black')
elif a>18 and a<29 : 
    if a%2==0 : print('black')
    else : print('red')
elif a>28 and a<37 : 
    if a%2==0 : print('red')
    else : print('black') 

