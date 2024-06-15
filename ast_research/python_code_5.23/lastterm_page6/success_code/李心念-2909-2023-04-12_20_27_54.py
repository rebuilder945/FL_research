list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
num = [int(x[0]) for x in list]
a = eval(input())
l = 0
r = len(num)-1
m = num[int((l+r)/2)]
def xunhuan():
    if a==num[m]:
        return list[m]
    elif a == num[r]:
        return list[r]
    elif a > num[m]:
        l = m 
        m = num[int((l+r)/2)]
        xunhuan()
    elif a < num[m]:
        r = m
        m = num[int((l+r)/2)]
        xunhuan()
b = xunhuan()
s = b[0]+b[1]
print(b)
