k=input()
left=0
right=19
m=int((left+right)/2)
stu=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],
['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],
['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],
['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],
['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
while left<=right:
    if k not in ["201801","201802","201803","201804","201805","201806","201807","201808","201809","201810","201811","201812","201813","2018014","201815","201816","201817","201818","201819","201820"]:
        print("None")
        break
    elif stu[m][0]<k:
        left=m-1
        m=int((left+right)/2)
    elif stu[m][0]>k:
        right=m+1
        m=int((left+right)/2)
    else:
        print(stu[m][0]+stu[m][1])
        break
