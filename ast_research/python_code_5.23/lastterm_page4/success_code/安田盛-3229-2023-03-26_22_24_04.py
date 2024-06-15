# lst=eval(input())
# a=[]
# for i in lst:
#     if lst.count(i)==1:
#         a.append(i)
# a.sort()
# if a==[]:
#     print("False")
# else:
#     print(*a,sep=",")

lst=eval(input())
a=[]
for i in lst:
    if lst.count(i)==1:
        a.append(i)
a.sort()
if a==[]:
    print("False")
else:
    for i in range(len(a)):
        if i==len(a)-1:
            print(a[i])
        else:
            print(a[i],end=",")
