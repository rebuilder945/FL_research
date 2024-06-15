a=eval(input())
list1=list(range(1,a+1))
b=0
c=0
for x in list1:
    if b==0:
        c=x
        list1[b]=list1[b+1]
        b+=1
    elif b==len(list1)-1:
        break
    else:
        list1[b]=list1[b+1]
        b+=1
list1[b]=c
print(list1)

