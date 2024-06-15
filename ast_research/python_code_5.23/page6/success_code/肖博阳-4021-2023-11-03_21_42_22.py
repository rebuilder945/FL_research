list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
n=eval(input())
begin=1
end=len(list)
while begin<=end:
    mid=(begin+end)/2
    if (n-201800)==mid:
        print(list[n-201801][0]+list[n-201801][1])
        break
    elif (n-210800)<mid and (n-201800)>=1:
        end=mid-1
        
    elif n-201800>mid and n<=201820:
        begin=mid+1
    else:
        print("None")
        break 
       
    


