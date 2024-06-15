stu_list=\
[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],
['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],
['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],
['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],
['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
# print(stu_list[0][0],type(int(stu_list[0][0])))
min=int(stu_list[0][0])
max=int(stu_list[19][0])
minnum=0
maxnum=19
search=int(input())
while 201801<=search<=201820:
    midnum=(minnum+maxnum)//2
    if search==int(stu_list[midnum][0]):
        print(stu_list[midnum][0]+stu_list[midnum][1])
        break
    elif search>=int(stu_list[midnum][0]):
        minnum=midnum+1
    else:
        maxnum=midnum-1
if search<201801 or search >201820:
    print("None")

