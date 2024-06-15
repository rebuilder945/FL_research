list1=eval(input())
a=sum(list1)
b=len(list1)
if a%b==0:
    print(int(a//b))
else :
    print( "%.2f" %(a/b))    
