stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],
['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],
['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],
['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],
['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]

# d=dict(stu_list)
n=eval(input())
# if n in d.keys():
#     print(d['n'])
# else:
#     print('None')
# if n  not in range(201801,201821):
#      print('None')
# else:
#     a=n
#     print(d['a'])
# print(d)
# print(d["n"])
if n not in range(201801,201821):
    print('None')
if n in range(201801,201821):
    print("".join(stu_list[n-201801]))
