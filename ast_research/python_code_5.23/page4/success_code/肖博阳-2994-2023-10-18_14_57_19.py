list=eval(input())
n,m=eval(input())
list2=[]
a=list[n]
if n<=len(list):
    i=0
    while i<m:
        list2.append(a)
        i+=1
    list.extend(list2)
    print(list)
else:
    print("error")
   
   

