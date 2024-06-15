stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
a=int(stu_list[0][0])
v=len(stu_list)-1
b=int(stu_list[v][0])
x=eval(input())
if x<a or x>b:
    print("None")
else:
    if a<b:
        c=(a+b)/2
        if x>c:
            a=c
        if x<=c:
            b=c
    if a==b:
        name=stu_list[a][1]
        kk=''
        kk=name+kk
        print(x+name)
        
