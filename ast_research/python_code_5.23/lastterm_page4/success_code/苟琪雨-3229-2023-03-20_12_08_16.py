list1=eval(input())
result=[]
flag=0
for i in list1:
    if list1.count(i)==1:
        result.append(i)
        flag+=1
if flag>0:
    result.sort()
    print(",".join(str(x) for x in result))
else:
    print("False")
        
