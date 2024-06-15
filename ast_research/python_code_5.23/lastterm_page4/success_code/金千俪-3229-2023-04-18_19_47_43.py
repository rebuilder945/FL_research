lst=eval(input())
lst1=[]
for x in lst:
    if lst.count(x)==1:
        lst1.append(x)
if len(lst1)==0:
    print("False")
else:
    lst1.sort()
    print(*lst1,sep=",")
    
        

#怎么把lst输出去掉列表的括号？
#为什么不对？
#for x in lst:
#    if lst.count(x)==1:
#        lst1.append(x)
#       print(lst1)
#  else:
#       print("False")
        
   



#lst[x]x表示下标，del，pop(x),insert(x,元素)，
