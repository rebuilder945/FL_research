lst=eval(input())
for x in lst:
    if lst.count(x)==1:
        lst.sort()
        for x in lst:
                print(x,end=',')
                break
for x in lst:
    if lst.count(x)>1:
        print("False")
        break

#怎么把lst输出去掉列表的括号？
#为什么不对？
#for x in lst:
#    if lst.count(x)==1:
#        lst1.append(x)
#       print(lst1)
#  else:
#       print("False")
        
   



#lst[x]x表示下标，del，pop(x),insert(x,元素)，
