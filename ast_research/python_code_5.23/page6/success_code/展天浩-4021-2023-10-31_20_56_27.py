stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
begin=0
end=len(stu_list)-1
a=int(input())
c=0
while begin<end:
    b=(begin+end)//2
    if a==int(stu_list[b][0]):
        for i in stu_list[b]:
            print(i,end="")
            c=1
        break    
    elif a>int(stu_list[b][0]):
        begin=b+1
    elif a<int(stu_list[b][0]):
        end=b-1
if c==0:
    print("None")
