a=eval(input())
stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
if a<201801 or a>201820:
        print(None)
else:
        b=int(a)-201800
        c=stu_list[b-1][0]+stu_list[b-1][1]
        print(eval(c))
        
