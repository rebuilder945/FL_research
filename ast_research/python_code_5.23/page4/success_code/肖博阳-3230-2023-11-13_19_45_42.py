list=eval(input())
list.sort(reverse=True)
if list[0]==0:
    print(0)
else:
    for i in list:
        print(i,end="")
            
    
