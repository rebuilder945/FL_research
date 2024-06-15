list1=eval(input())
list1.sort(reverse=True)
if list1[0] in ['0']:
     print("0")
else :
    for x in list1:    
     print(x,end="")
