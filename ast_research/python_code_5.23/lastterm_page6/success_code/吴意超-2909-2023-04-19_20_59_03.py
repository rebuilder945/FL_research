def a(b,c):
    l = 0
    r = len(b) -1
    while(l <= r):
        m = (l + r)/2
        if(int(b[m][0])==c):
            return m
        elif c < int(b[m][0]):
            r = m - 1
        else:
            l = m + 1
    return -1
b = [['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
c = eval(input())
m = a(b,c)
if m == -1:
    d = "None"
else:
    d = a[m][0] + a[m][1]
print(d)
