lst1=input().split()
lst2=[float(lst1[1]),float(lst1[2]),float(lst1[3])]
lst2.sort(reverse=True)
a=float(lst2[0])
b=float(lst2[1])
c=float(lst2[2])
avg=(a+b+c)/3
print("%s %.2f %.2f %.2f %.2f"%(lst1[0],a,b,c,avg))
