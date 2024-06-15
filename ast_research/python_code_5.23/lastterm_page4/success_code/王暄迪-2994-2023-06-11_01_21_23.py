lst1=input().split(",")
lst2=input().split(",")
n=int(lst2[0])
m=int(lst2[1])
if n>=0 and n <=len(lst1)-1:
    for i in range(m):
        lst1.append(lst1[n])
    print(lst1)
elif n<0 and -n<=len(lst1):
    for i in range(m):
        lst1.append(lst1[n])
    print(lst1)
else:
    print("error")
