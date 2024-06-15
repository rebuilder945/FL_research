list1=eval(input())
a,b=eval(input())
if a in list1 and b in list1:
    del list1[a:b]
    
    print(list1)
elif not a in list1 or not b in list1:
    print("error")    



