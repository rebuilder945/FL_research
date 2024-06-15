list=[]
list.append(eval(input()))
count=1
flag=True
while flag==True:
    add=input()
    if add!="#":
        list.append(add)
        count=count+1
    else:
        flag=False
        break
lis=map(int,list)
a=sum(lis)
print(count,"",a)
