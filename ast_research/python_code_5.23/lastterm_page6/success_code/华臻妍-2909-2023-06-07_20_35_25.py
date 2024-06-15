#折半查找法，数据分成两份进行比较后类推
def search(lst,num):
    low=0#指列表中第一个元素
    high=len(lst)-1
    while low<=high:
        mid=(high+low)//2
        if num<int(lst[mid][0]):
            high=mid-1#记住！
        elif num>int(lst[mid][0]):
            low=mid+1
        else:
            return mid
    return False
stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]

num=eval(input())
if search(stu_list,num):
    temp=search(stu_list,num)#temp就是变量
    print("".join(stu_list[temp]))
else:
    print(None)

