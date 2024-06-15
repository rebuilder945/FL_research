def zb(a):
    b,e=0,len(m)-1
    while b<=e:
        mid=(b+e)//2
        if a==m[mid]:
            print("".join(stu_list[mid]))
            break
        elif  int(a)>int(m[mid]):
            b=mid+1
        else:
            e=mid-1
    else:
        print("未找到该学生")
n=input()
stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
m=[]
for x in stu_list:
    m.append(x[0])
zb(n)
