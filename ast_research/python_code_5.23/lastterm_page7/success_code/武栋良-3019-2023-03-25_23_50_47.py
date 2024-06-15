lst = input().split()
lst1 = list(map(int,[lst[1],lst[2],lst[3]]))
lst1.sort(reverse=True)
a = int(lst1[0])
b = int(lst1[1])
c = int(lst1[2])
d = (a+b+c)/3
print("%s %.2f %.2f %.2f %.2f"%(lst[0],a,b,c,d))




