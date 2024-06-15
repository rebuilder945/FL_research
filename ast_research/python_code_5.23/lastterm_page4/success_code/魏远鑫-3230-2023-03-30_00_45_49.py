list=eval(input())
c=list.sort()
b=list.reverse()
for i in range(0,len(list)):
    a=list[i]
    if list[i]==0:
        print("")
    else:    
        print(a,end="")


