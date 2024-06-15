x=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
a=eval(input())
b=[]
for i in range(len(x)):
    b.append(x[i][0])
    c=list(map(int,b))
if a not in c:
    print("None")
else:
    l=0
    r=len(x)-1
    while(l<=r):
        m=(l+r)//2
        if a==c[m]:
            print(x[m])
        elif a<c[m]:
            r=m-1
        else:
            l=m+1

