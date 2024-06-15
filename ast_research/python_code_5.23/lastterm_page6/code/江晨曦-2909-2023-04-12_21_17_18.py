# #1
# a = input()
# b = ""
# for i in a:
#     if (int(i)+5)%10 !=0:
#         b = b+str((int(i)+5)%10)
#     else :
#         b = b+"0"
# b= b[::-1]
# print(b)

# #2
# a =eval(input())
# b =eval(input())
# s = a
# for i in range(b-1):
#     s+= a/2**i
# print('%.2f'%s)

#3
stu_list =

[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
a = eval(input())
def search(stu_list,a):
    left = 0
    right = len(stu_list)-1
    while (left<=right):
        mid = (left+right)/2
        if (int(stu_list[mid][o]==a)):
            return mid
        elif a<int(stu_list[mid][0]):
            right = mid-1
        else:
            left = mid-1
mid = search(stu_list,a)
if mid == -1:
    strl ="None"
else:
    strl = stu_list[mid][0]+stu_list[mid][1]
print(strl)
