list1=eval(input())
n,m=eval(input())
list2=list(list1)
if n>=0 and n>len(list1)-1:
    print("error")
if n<0:
    n=len(list1)+n
    if n<0:
        print("error")
    else:
        k=list2[n]
        for i in range(m):
            list2=list2+[k]
    print(list2)
else:
    if n>=0 and n<=len(list1)-1:
        k=list2[n]
        for x in range(m):
            list2=list2+[k]
        print(list2)

