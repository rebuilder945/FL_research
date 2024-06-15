x=input().split(",")
list=list(map(int,x))#此处x不可命名为list，混淆
n,m=eval(input())
a=len(list)
# list1=[]正确
if n>(a-1) or n<0:
    print("error")
else:
    list1=[]#正确
    for i in range(m):
        # list1=[]错误，每次循坏都会把list1清空
        list1.append(list[n])
    list2=list+list1
    print(list2)

   
