lst1=eval(input())
lst2=eval(input()).split(",")
n=int(lst2[0])
m=int(lst2[1])
if n>=0 and n <=len(lst1)-1:
    for i in range(m):
        lst1.append(lst1[n])
elif n<0 and -n<=lem(lst1):
    for i in range(m):
        lst1.append(lst1[n])
else:
    print("error")
