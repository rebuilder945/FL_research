a=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],
['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],
['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],
['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],
['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
b=len(a)
n=input()
d=[]
for i in range(b):
    if n==a[i][0]:
        d.append(a[i])
    else:
        pass
if d==[]:
    print(None)
else:
    for i in d:
        if type(i)==list:
            d.extend(i)
            d.remove(i)
    print(''.join(str(i)for i in d))
