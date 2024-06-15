stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
xuehao=eval(input())
if xuehao<201801 or xuehao>201820:
    print('None')
else:
    for x in len(stu_list):
        if xuehao in stu_list[x]:
            print(str(stu_list[x][0])+str(stu_list[x][1]))

