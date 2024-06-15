list=eval(input())
n,m=eval(input())
list2=[]
if n<=len(list):
    i=0
    while i<m:
        a=list[n]
        list2.append(a)
        i+=1
    
    print(list+list2)
else:
    print("error")
   
   

