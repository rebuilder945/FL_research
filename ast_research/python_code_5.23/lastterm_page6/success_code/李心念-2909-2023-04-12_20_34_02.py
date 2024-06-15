list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
num = [int(x[0]) for x in list]
a = eval(input())
def xunhuan(a,num):
    l = 0
    r = len(num)-1
    m = num[int((l+r)/2)]
    if a==num[m]:
        return m
    elif a == num[r]:
        return r
    elif l == m:
        return -1
    elif a > num[m]:
        l = m 
        m = num[int((l+r)/2)]
        xunhuan()
    elif a < num[m]:
        r = m
        m = num[int((l+r)/2)]
        xunhuan()
b = xunhuan(a,num)
if b == -1:
    print('None')
else:
    s = list[b][0]+list[b][1]
    print(s)
