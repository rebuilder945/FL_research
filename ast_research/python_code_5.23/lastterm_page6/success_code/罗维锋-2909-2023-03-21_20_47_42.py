def search(arr,m,r,x):
    if r>=m:
        mid=int(m+(r-1)/2)
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return search(arr,m,mid-1,x)
        else:
            return search(arr,mid+1,r,x)
    else:
        return -1

a=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
b=eval(input())
c=list(map(int,[a[x][0] for x in range(len(a))]))
result=search(c,0,len(c)-1,b)
if result!= -1:
    print(a[result][0]+a[result][1])
else:
    print("None")
    

