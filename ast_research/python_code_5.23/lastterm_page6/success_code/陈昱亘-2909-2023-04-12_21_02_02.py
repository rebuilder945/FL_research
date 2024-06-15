stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
num=eval(input())
a=201801
b=201820
while a<b:
    if num==(a+b)//2:
        print(''.join(stu_list[((a+b)//2)%100-1]))
        break
    elif a<=num<(a+b)//2:
        b=(a+b)//2-1
    elif (a+b)//2<num<=b:
        a=(a+b)//2+1
    else: print('None')
