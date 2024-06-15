ls=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
xuehao=eval(input())
xuehao=str(xuehao)
for i in range(len(ls)):
    if xuehao in ls[i]:
        print(ls[i][0],end="")
        print(ls[i][1])
xuehao=int(xuehao)
if xuehao<201801 or xuehao>201820:
    print("None")
