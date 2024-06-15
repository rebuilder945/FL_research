list1=eval(input())
list2=[]
for i in list1:
    n=list1.count(i)
    if n==1:
        list2.append(i)
print(list2)
if list2==[]:
    print("False")

