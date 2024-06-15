a=list(input().split(" "))
num=[int(a[1]),int(a[2]),int(a[3])]
num.sort(reverse=True)
c=(eval(a[1])+eval(a[2])+eval(a[3]))/3
print("%s %.2f %.2f %.2f %.2f" %(a[0],num[0],num[1],num[2],c))

