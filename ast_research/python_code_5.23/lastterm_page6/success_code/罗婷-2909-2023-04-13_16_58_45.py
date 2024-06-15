def ifind(x,y):
    length=len(x)
    lst=x[:length//2]
    if y==int(lst[-1][0]):
        return lst[-1]
    elif y<int(lst[-1][0]):
        return ifind(lst,y)
    else:
        return ifind(x[length//2:length],y)
stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
a=eval(input())
if a<int(stu_list[0][0]) or a>int(stu_list[-1][0]):
    print('None')
else:
    m=ifind(stu_list,a)
    for x in m:
        print(x,end='')




