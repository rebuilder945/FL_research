list=eval(input())
c=list.sort()
b=list.reverse()
for i in range(0,len(list)):
    a=list[i]
    if list[0]==0:
        print("0")
    else:    
        print(a,end="")


