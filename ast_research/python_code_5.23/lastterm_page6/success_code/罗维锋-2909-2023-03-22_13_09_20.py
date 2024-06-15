def search(num,low,high,m):
    result=-1
    while low<=high:
        mid=(low+high)//2
        if m<num[mid]:
            high=mid-1
        else:
            if m>a[mid]:
                low=mid+1
            else:
                result=mid
                break
    return result
    
a=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
b=eval(input())
c=list(map(int,[a[x][0] for x in range(len(a))]))
result=search(c,0,len(c)-1,b)
if result!= -1:
    print(a[result][0]+a[result][1])
else:
    print("None")
    

