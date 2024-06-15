stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],
['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],
['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],
['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],
['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
a=input()
b=len(stu_list)
c=1
while c<=b:
    if c==b==mid:
        c=c+2
    mid=(b+c)//2
    if a==stu_list[mid][0]:
        print(stu_list[mid][0]+stu_list[mid][1])
        break
    elif int(stu_list[mid][0]) >int(a):
        b=b-1
    elif int(stu_list[mid][0]) <int(a):
        c=mid
else:
    print("None")
    
