list1=eval(input())
n=[]
for x in list1[:]:
    if list1.count(x)==1:
        n.append(x)
n.sort
if n==[]:
    print("False")
else :
    for x in n[0:-1]:
        print(x,end=',')
    for x in n[-1:]:
        print(x,end="")



