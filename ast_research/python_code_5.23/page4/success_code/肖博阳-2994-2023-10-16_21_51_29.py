list=eval(input())
n,m=eval(input())
list2=[]
a=list[n-1]
if n<=len(list):
    i=0
    while i<m:
        list2.append(a)
        i+=1
else:
    print("error")
list.extend(list2)    
print(list)    

